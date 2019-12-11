# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import os
import re
from operator import itemgetter, attrgetter
from typing import List, Iterator, Union, NamedTuple, Optional, Tuple, Dict
from collections import OrderedDict

SPACE_4 = " " * 4
SPACE_8 = " " * 8
SPACE_12 = " " * 12

LICENSE = """# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
"""

TRADER_API_PXD_DEFAULT_LINES = """
cdef extern from "ThostFtdcTraderApi.h":
    cdef cppclass CTraderApi "CThostFtdcTraderApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil"""

TRADER_API_PXD_ADDITIONAL_LINES = """cdef extern from "ThostFtdcTraderApi.h" namespace "CThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath) nogil except +
    const_char *GetApiVersion() nogil


cdef extern from "CTraderSpi.h":
    cdef cppclass CTraderSpi:
        CTraderSpi(PyObject *obj)"""

TRADER_API_DEFAULT_PYX_LINES = """cdef class TraderApi:
    cdef CTraderApi *_api
    cdef CTraderSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __init__(self, const_char *pszFlowPath):
        self._api = CreateFtdcTraderApi(pszFlowPath)
        if self._api is NULL:
            raise MemoryError()
        self._spi = new CTraderSpi(<PyObject *>self)
        if self._spi is NULL:
            raise MemoryError()
        self._api.RegisterSpi(self._spi)

    def __dealloc__(self):
        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def _ensure_api_not_null(self):
        if self._api is NULL:
            raise MemoryError()

    def Release(self):
        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def Join(self):
        cdef int result
        self._ensure_api_not_null()
        if self._spi is not NULL:

            print("before api join")
            with nogil:
                result = self._api.Join()
            return result

"""

RE_CONST = r"THOST_FTDC_([\d\w]+)_(?P<name>[\d\w]+)"
RE_API_METHOD = r"virtual (?P<return_type>[\w]+) (?P<name>[\d\w]+)\((?P<params>[\d\w\s\*,]*)\) = 0;"
RE_SPI_METHOD = r"virtual void (?P<name>[\d\w]+)\((?P<params>[\d\w\s\*,]*)\)( )?{};"


class Constant(NamedTuple):
    name: str
    value: str
    comment: str
    
    @property
    def py_const_name(self):
        name = re.match(RE_CONST, self.name).group("name")
        if name == "None" or re.match(r"^\d+", name):
            name = "_" + name
        return name


class CustomType(NamedTuple):
    base_type: str
    array_len: Optional[int]
    name: str
    enum_values: List[Constant]
    comment: str
    
    @property
    def py_enum_class_name(self):
        return re.match(r"TThostFtdc(?P<name>[\d\w]+)Type", self.name).group("name")
    
    @property
    def py_type(self):
        if self.base_type == "char":
            return "str"
        return {
            "short": "int", "int": "int", "long": "int", "double": "float"
        }[self.base_type]


class EnumType(NamedTuple):
    name: str
    items: List[Tuple[str, str]]


class StructMember(NamedTuple):
    name: str
    type: CustomType
    comment: str


class StructType(NamedTuple):
    name: str
    members: List[StructMember]
    comment: str
    
    @property
    def py_class_name(self):
        return re.match(r"CThostFtdc(?P<name>[\d\w]+)Field", self.name).group("name")


class Parameter(NamedTuple):
    name: str
    type: Union[str, StructType]
    pointer: bool

    def to_api_pxd_line(self):
        if self.type == "CThostFtdcTraderSpi":
            type_ = "CTraderSpi"
        elif isinstance(self.type, str):
            type_ = self.type
        else:
            type_ = self.type.name
        if self.pointer:
            return f"{type_} *{self.name}"
        else:
            return f"{type_} {self.name}"

    def to_api_pyx_method_signature(self):
        return self.to_api_pxd_line()


class Method(NamedTuple):
    name: str
    return_type: str
    params: List[Parameter]
    comments: List[str]

    def to_api_pxd_line(self):
        return "{} {}({}) nogil except +".format(
            self.return_type, self.name, ", ".join([p.to_api_pxd_line() for p in self.params])
        )

    def to_api_pyx_lines(self):
        yield "def {}({});".format(
            self.name, ", ".join(["self"] + [p.to_api_pyx_method_signature() for p in self.params])
        )
        if self.return_type == "void":
            yield "self._ensure_api_not_null()"
            yield "self._api."


class Api(NamedTuple):
    methods: List[Method]

    def to_api_pyx_lines(self):
        pass

    def to_api_pxd_lines(self):
        for l in TRADER_API_PXD_DEFAULT_LINES.split("\n"):
            yield l
        for method in self.methods:
            if method.name in ("Release", "Init", "Join"):
                continue
            yield SPACE_8 + method.to_api_pxd_line()


def is_comment(line: str):
    return line.startswith("/")


def parse_comment(line: str, remove_suffix=False):
    try:
        line = line.split("是一个")[1]
    except IndexError:
        line = line.replace("/", "")

    if remove_suffix:
        if line.endswith("类型"):
            line = line[:-2]
    return line


def is_constant_declaration(line: str):
    return line.startswith("#define ")


def parse_constant_declaration(line: str, comment: str):
    _, name, value = line.split()
    return Constant(name, value, comment)


def is_type_def(line: str):
    return line.startswith("typedef ")


def parse_type_def(line: str, enum_values, comment: str):
    _, base_type, name = line.split(";")[0].split()
    try:
        (name, array_len), = re.findall(r"(.+)\[(\d+)\]", name)
    except ValueError:
        array_len = None
    if enum_values:
        assert base_type == "char"
    return CustomType(base_type, array_len, name, enum_values, comment)


def parse_struct_def(first_line: str, line_iter: Iterator[str], comment: str, type_dict: dict):
    assert first_line.startswith("struct ")
    name = first_line.split()[1]
    members = []
    line = next(line_iter)
    assert line == "{"
    last_comment = None
    while True:
        line = next(line_iter)
        if line == "};":
            break
        elif is_comment(line):
            last_comment = parse_comment(line)
        else:
            member_type_name, member_name = line[:-1].split()
            members.append(StructMember(member_name, type_dict[member_type_name], last_comment))
    return StructType(name, members, comment)


def useless(l):
    return len(l.strip().replace("/", "")) == 0


def line_gen(raw_lines):
    for l in raw_lines:
        if not useless(l):
            yield l.strip()


def parse_data_type_header(raw_lines: List[str]):
    last_comment = None
    comment = None
    constants = []

    lines = line_gen(raw_lines)

    while True:
        try:
            l = next(lines)
        except StopIteration:
            break
        if "THOST_FTDCDATATYPE_H" in l:
            comment = ""
            continue
        if is_comment(l):
            last_comment = parse_comment(l, True)
            if not comment:
                comment = last_comment
        elif is_constant_declaration(l):
            constants.append(parse_constant_declaration(l, last_comment))
        elif is_type_def(l):
            yield parse_type_def(l, constants.copy(), comment)
            comment = None
            constants.clear()
        elif l.startswith("enum"):
            assert next(lines) == "{"
            while next(lines) != "};":
                continue
        elif l == "#endif":
            break
        else:
            raise RuntimeError(f"Bad line: {l}")


def parse_struct_header(raw_lines: List[str], type_dict: dict):
    lines = line_gen(raw_lines)
    comment = None
    while True:
        line = next(lines)
        if is_comment(line):
            comment = parse_comment(line)
        elif line.startswith("struct "):
            yield parse_struct_def(line, lines, comment, type_dict)


def parse_trader_api_header(raw_lines: List[str], struct_dict: Dict[str, StructType]):
    def _parse_params(params: str):
        if params:
            for param in (params.split(",") if "," in params else [params]):
                param = param.strip()
                param_elements = param.split(" ")
                pointer = False
                if "*" in param_elements:
                    param_elements.remove("*")
                    pointer = True
                param_type, param_name = param_elements
                if param_name.startswith("*"):
                    param_name = param_name.split("*")[1]
                    pointer = True
                elif param_type not in {"int", "bool", "char", "CThostFtdcTraderSpi", "THOST_TE_RESUME_TYPE"}:
                    param_type = struct_dict[param_type]
                yield Parameter(name=param_name, type=param_type, pointer=pointer)

    def _parse_api(line_iter: Iterator[str]):
        assert next(line_iter) == "{"
        assert next(line_iter) == "public:"
        comments = []
        while True:
            l = next(line_iter)
            if l == "protected:":
                assert next(line_iter) == "~CThostFtdcTraderApi(){};"
                assert next(line_iter) == "};"
                break
            elif l.startswith("///"):
                comments.append(l.split("///")[1])
            elif re.match(RE_API_METHOD, l):
                name, return_type, params = itemgetter("name", "return_type", "params")(
                    re.match(RE_API_METHOD, l).groupdict()
                )
                yield Method(name=name, return_type=return_type, params=list(_parse_params(params)), comments=comments)
                comments.clear()
            elif l.startswith("static") or l.startswith("virtual const"):
                comments.clear()
            else:
                raise RuntimeError(f"Bad line: {l}")

    def _parse_spi(line_iter: Iterator[str]):
        assert next(line_iter) == "{"
        assert next(line_iter) == "public:"
        comments = []
        while True:
            l = next(line_iter)
            if l == "};":
                break
            elif l.startswith("///"):
                comments.append(l.split("///")[1])
            elif re.match(RE_SPI_METHOD, l):
                name, params = itemgetter("name", "params")(re.match(RE_SPI_METHOD, l).groupdict())
                yield Method(name=name, return_type="void", params=list(_parse_params(params)), comments=comments)
                comments.clear()
            else:
                raise RuntimeError(f"Bad line: {l}")

    lines = line_gen(raw_lines)

    api, spi = None, None
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break
        if line == "class TRADER_API_EXPORT CThostFtdcTraderApi":
            api = Api(methods=list(_parse_api(lines)))
        elif line == "class CThostFtdcTraderSpi":
            spi = Api(methods=list(_parse_spi(lines)))
        else:
            pass
    if not (api and spi):
        raise RuntimeError("{} not found".format("api" if api is None else "spi"))
    return spi, api


class PyCodeGenerator(object):
    def __init__(self, api_path):
        self._types: OrderedDict[str, Union[CustomType, EnumType]] = OrderedDict()
        self._structs = OrderedDict()
        self._trader_spi = None
        self._trader_api = None

        with open(os.path.join(api_path, "ThostFtdcUserApiDataType.h"), encoding="GBK") as f:
            for type_obj in parse_data_type_header(f.readlines()):
                self._types[type_obj.name] = type_obj

        with open(os.path.join(api_path, "ThostFtdcUserApiStruct.h"), encoding="GBK") as f:
            for struct_obj in parse_struct_header(f.readlines(), self._types):
                self._structs[struct_obj.name] = struct_obj

        with open(os.path.join(api_path, "ThostFtdcTraderApi.h"), encoding="GBK") as f:
            self._trader_spi, self._trader_api = parse_trader_api_header(f.readlines(), self._structs)

    def write(self, py_path):
        from jinja2 import Environment, FileSystemLoader

        if not os.path.exists(py_path):
            os.makedirs(py_path)

        file_loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
        env = Environment(loader=file_loader)
        env.trim_blocks = True
        env.lstrip_blocks = True
        env.rstrip_blocks = True

        with open(os.path.join(py_path, "ThostFtdcUserApiDataType.pxd"), "w+", encoding="utf-8") as f:
            template = env.get_template("ThostFtdcUserApiDataType.pxd.jinja")
            f.write(template.render(types=self._types.values()))

        with open(os.path.join(py_path, "ThostFtdcUserApiStruct.pxd"), "w+", encoding="utf-8") as f:
            template = env.get_template("ThostFtdcUserApiStruct.pxd.jinja")
            f.write(template.render(structs=self._structs.values()))

        with open(os.path.join(py_path, "structs.py"), "w+", encoding="utf-8") as f:
            template = env.get_template("structs.py.jinja")
            f.write(template.render(
                char_array_lengths=sorted(set(t.array_len for t in self._types.values() if t.array_len), key=int),
                structs=self._structs.values()
            ))

        with open(os.path.join(py_path, "structs.pyi"), "w+", encoding="utf-8") as f:
            template = env.get_template("structs.pyi.jinja")
            f.write(template.render(structs=self._structs.values()))

        with open(os.path.join(py_path, "consts.py"), "w+", encoding="utf-8") as f:
            template = env.get_template("consts.py.jinja")
            f.write(template.render(enum_types=[t for t in self._types.values() if t.enum_values]))

        with open(os.path.join(py_path, "ThostFtdcTraderApi.pxd"), "w+", encoding="utf-8") as f:
            lines = [
                LICENSE, "from cpython cimport PyObject", "from libc.string cimport const_char", "",
                "from .ThostFtdcUserApiStruct cimport *", ""
            ]
            lines.extend(list(self._trader_api.to_api_pxd_lines()) + [""] * 2)
            lines.append(TRADER_API_PXD_ADDITIONAL_LINES)
            f.writelines([l + "\n" for l in lines])


if __name__ == "__main__":
    PyCodeGenerator("ctp").write("rqctp")
