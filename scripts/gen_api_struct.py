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
from operator import itemgetter
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

    def Init(self):
        self._ensure_api_not_null()
        self._api.Init()

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

    def to_consts_py_line(self, is_bytes: bool):
        name = re.match(RE_CONST, self.name).group("name")
        if name == "None" or re.match(r"^\d+", name):
            name = "_" + name
        value = self.value
        if is_bytes:
            value = f"{self.value}"
        return "{} = {}  # {}".format(name, value, self.comment)


class CustomType(NamedTuple):
    base_type: str
    array_len: Optional[int]
    name: str
    enum_values: List[Constant]
    comment: str

    def to_pxd_line(self):
        line = f"ctypedef {self.base_type} {self.name}"
        if self.array_len:
            line += f"[{self.array_len}]"
        line += f"  # {self.comment}"
        return line

    def to_consts_py_lines(self):
        if not self.enum_values:
            return
        yield "\n"
        class_name = re.match(r"TThostFtdc(?P<name>[\d\w]+)Type", self.name).group("name")
        yield f"class {class_name}:  # {self.comment}"
        for const in self.enum_values:
            yield SPACE_4 + const.to_consts_py_line(self.base_type == "char")

    def to_py_ctype(self):
        if self.array_len:
            if self.base_type == "char":
                return f"c_char_Array_{self.array_len}"
            else:
                raise NotImplementedError
        else:
            return f"c_{self.base_type}"

    def to_py_type(self):
        if self.base_type == "char":
            if self.enum_values:
                return "bytes"
            return "str"
        return {
            "short": "int", "int": "int", "long": "int", "double": "float"
        }[self.base_type]


class EnumType(NamedTuple):
    name: str
    items: List[Tuple[str, str]]

    def to_pxd_lines(self):
        yield f"cdef enum {self.name}:"
        for name, value in self.items:
            py_line = SPACE_4 + name
            if value:
                py_line += f" = {value}"
            yield py_line

    def to_consts_py_lines(self):
        yield f"class {self.name[9:]}:"
        last_value = "0"
        for name, value in self.items:
            if not value:
                value = str(int(last_value) + 1)
            yield SPACE_4 + "{} = {}".format(name.split("_")[-1], value)
            last_value = value


class StructMember(NamedTuple):
    name: str
    type: CustomType
    comment: str

    def to_pxd_line(self):
        return f"{self.type.name} {self.name}  # {self.comment}"


class StructType(NamedTuple):
    name: str
    members: List[StructMember]
    comment: str

    def to_pxd_lines(self):
        yield f"cdef struct {self.name}:  # {self.comment}"
        for member in self.members:
            yield SPACE_4 + member.to_pxd_line()

    def to_py_lines(self):
        def _field_declare():
            yield SPACE_4 + "_fields_ = ["
            for member in self.members:
                yield SPACE_8 + f"(\"{member.name}\", {member.type.to_py_ctype()}),"
            yield SPACE_4 + "]"

        def _init_body():
            yield SPACE_8 + "super().__init__()"
            for member in self.members:
                yield SPACE_8 + "if {}:".format(member.name)
                if member.type.to_py_type() == 'str':
                    yield SPACE_12 + "self.{} = {}.encode(\"GBK\")".format(member.name, member.name)
                else:
                    yield SPACE_12 + "self.{} = {}".format(member.name, member.name)

        class_name = re.match(r"CThostFtdc(?P<name>[\d\w]+)Field", self.name).group("name")

        yield f"class {class_name}(Struct):"
        yield from _field_declare()
        yield ""
        yield SPACE_4 + "def __init__({}):".format(", ".join(["self"] + [m.name + "=None" for m in self.members]))
        yield from _init_body()

    def to_pyi_lines(self):
        def _init_header():
            class_name = re.match(r"CThostFtdc(?P<name>[\d\w]+)Field", self.name).group("name")
            yield f"class {class_name}(Struct):"
            yield SPACE_4 + "def __init__("
            yield SPACE_8 + "self,"
            for member in self.members:
                yield SPACE_8 + "{}: {} = None,".format(member.name, member.type.to_py_type())
            yield SPACE_4 + "):"

        def _init_comment():
            yield SPACE_8 + "\"\"\""
            yield SPACE_8 + self.comment
            for member in self.members:
                yield SPACE_8 + f":param {member.name}: {member.comment}"
            yield SPACE_8 + "\"\"\""

        yield from _init_header()
        yield from _init_comment()
        yield SPACE_8 + "super().__init__()"
        yield SPACE_8 + "..."

    def get_py_types(self):
        return {m.type.to_py_ctype() for m in self.members}


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


class Method(NamedTuple):
    name: str
    return_type: str
    params: List[Parameter]
    comments: List[str]

    def to_api_pxd_line(self):
        return "{} {}({}) nogil except +".format(
            self.return_type, self.name, ", ".join([p.to_api_pxd_line() for p in self.params])
        )


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
    return CustomType(base_type, array_len, name, enum_values, comment)


def is_enum_def(line: str):
    return line.startswith("enum")


def parse_enum_def(first_line: str, line_iter: Iterator[str]):
    name = first_line.split()[1]
    items = []
    assert next(line_iter) == "{"
    while True:
        line = next(line_iter)
        if line == "};":
            break
        m = re.match(r"^(?P<name>\w+)( = (?P<value>\d+))?(,)?$", line)
        if not m:
            raise RuntimeError(f"cannot parse lines: {line}")
        items.append((m.groupdict()["name"], m.groupdict()["value"]))
    return EnumType(name, items)


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
        elif is_enum_def(l):
            yield parse_enum_def(l, lines)
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


def gen_py_struct_lines(struct: StructType):
    name = struct.name[10:]
    if name.endswith("Field"):
        name = name[:-5]
    yield f"class {name}(BaseStruct): #{struct.comment}"
    yield "    def __init__(self, {}):".format(

        ", ".join(["{}={}".format(
            mem.name, 0 if mem.type.base_type in {"int", "short", "float", "double"} else "''"
        ) for mem in struct.members])
    )
    for member in struct.members:
        yield f"        self.{member.name} = '{member.type.name[10:-4]}' #{member.comment}, {member.type.base_type}"


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
        if not os.path.exists(py_path):
            os.makedirs(py_path)

        with open(os.path.join(py_path, "ThostFtdcUserApiDataType.pxd"), "w+", encoding="utf-8") as f:
            lines = [LICENSE, "", "cdef extern from \"ThostFtdcUserApiDataType.h\":"]
            for t in self._types.values():
                if isinstance(t, CustomType):
                    lines.append(SPACE_4 + t.to_pxd_line())
                elif isinstance(t, EnumType):
                    lines.extend([SPACE_4 + l for l in t.to_pxd_lines()])
                else:
                    raise RuntimeError(f"bad type: {t}")
            f.writelines([l + "\n" for l in lines])

        with open(os.path.join(py_path, "ThostFtdcUserApiStruct.pxd"), "w+", encoding="utf-8") as f:
            lines = [LICENSE, "from .ThostFtdcUserApiDataType cimport *", "", "cdef extern from \"ThostFtdcUserApiStruct.h\":"]
            for s in self._structs.values():
                for line in s.to_pxd_lines():
                    lines.append(SPACE_4 + line)
            f.writelines([l + "\n" for l in lines])

        with open(os.path.join(py_path, "structs.py"), "w+", encoding="utf-8") as f:
            lines = [LICENSE]
            base_py_types = set()
            array_py_types = set()
            for s in self._structs.values():
                for m in s.members:
                    py_type = m.type.to_py_ctype()
                    if "Array" in py_type:
                        array_py_types.add(py_type)
                    else:
                        base_py_types.add(py_type)
            if base_py_types:
                lines.append("from ctypes import {}".format(", ".join(base_py_types)))
            lines.append("\nfrom .utils import Struct\n")
            for py_type in sorted(array_py_types, key=lambda t: int(t.split("_")[-1])):
                lines.append("{} = {} * {}".format(py_type, *py_type.split("_Array_")))

            for s in self._structs.values():
                lines.extend([""] * 2)
                for line in s.to_py_lines():
                    lines.append(line)
            f.writelines([l + "\n" for l in lines])

        with open(os.path.join(py_path, "structs.pyi"), "w+", encoding="utf-8") as f:
            lines = [LICENSE, "", "from .utils import Struct"]
            for s in self._structs.values():
                lines.extend([""] * 2)
                for line in s.to_pyi_lines():
                    lines.append(line)
            f.writelines([l + "\n" for l in lines])

        with open(os.path.join(py_path, "consts.py"), "w+", encoding="utf-8") as f:
            lines = [LICENSE]
            for s in self._types.values():
                lines.extend(list(s.to_consts_py_lines()))
            f.writelines([l + "\n" for l in lines])

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
