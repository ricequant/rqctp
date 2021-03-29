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

RE_CONST = r"THOST_FTDC_([\d\w]+)_(?P<name>[\d\w]+)"
RE_API_METHOD = r"virtual (?P<return_type>[\w]+) (?P<name>[\d\w]+)\((?P<params>[\d\w\s\*\[\],]*)\) = 0;"
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


class ParameterType(NamedTuple):
    base: str
    pointer: bool
    array: bool
    primitive_base: bool


class Parameter(NamedTuple):
    name: str
    type: ParameterType

    @property
    def type_py_class_name(self):
        return re.match(r"CThostFtdc(?P<name>[\d\w]+)Field", self.type.base).group("name")


class Method(NamedTuple):
    name: str
    return_type: str
    params: List[Parameter]
    comments: List[str]


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
        try:
            line = next(lines)
        except StopIteration:
            break
        if is_comment(line):
            comment = parse_comment(line)
        elif line.startswith("struct "):
            yield parse_struct_def(line, lines, comment, type_dict)


def parse_api_header(raw_lines: List[str], structs: Dict) -> Tuple[List[Method], List[Method]]:
    def _parse_params(params: str):
        if params:
            for param in (params.split(",") if "," in params else [params]):
                yield _parse_param(param)

    def _parse_param(param: str):
        param = param.strip()
        param_elements = param.split(" ")
        pointer = array = False
        if "*" in param_elements:
            param_elements.remove("*")
            pointer = True
        param_type, param_name = param_elements
        if param_name.startswith("*"):
            param_name = param_name.split("*")[1]
            pointer = True
        if param_name.endswith("[]"):
            if param_type != "char":
                raise NotImplementedError(param)
            param_name = param_name.split("[]")[0]
            array = True

        if param_type in ("int", "char", "bool"):
            primitive_base = True
        else:
            if param_type not in structs:
                raise NotImplementedError(param_type)
            primitive_base = False

        return Parameter(name=param_name, type=ParameterType(
            base=param_type, pointer=pointer, array=array, primitive_base=primitive_base
        ))

    def _parse_api(line_iter: Iterator[str]):
        assert next(line_iter) == "{"
        assert next(line_iter) == "public:"
        comments = []
        while True:
            l = next(line_iter)
            if l == "protected:":
                assert next(line_iter) in ["~CThostFtdcTraderApi(){};", "~CThostFtdcMdApi(){};"]
                assert next(line_iter) == "};"
                break
            elif l.startswith("///"):
                comments.append(l.split("///")[1])
            elif re.match(RE_API_METHOD, l):
                name, return_type, params = itemgetter("name", "return_type", "params")(
                    re.match(RE_API_METHOD, l).groupdict()
                )
                if name in ("Init", "Release", "Join", "SubscribePrivateTopic", "SubscribePublicTopic", "RegisterSpi"):
                    continue
                params = list(_parse_params(params))
                yield Method(
                    name=name, return_type=return_type, params=params, comments=comments.copy()
                )
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
                yield Method(name=name, return_type="void", params=list(_parse_params(params)), comments=comments.copy())
                comments.clear()
            else:
                raise RuntimeError(f"Bad line: {l}")

    lines = line_gen(raw_lines)
    
    api_methods, spi_methods = None, None
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break
        if line in ["class TRADER_API_EXPORT CThostFtdcTraderApi", "class MD_API_EXPORT CThostFtdcMdApi"]:
            api_methods = list(_parse_api(lines))
        elif line in ["class CThostFtdcTraderSpi", "class CThostFtdcMdSpi"]:
            spi_methods = list(_parse_spi(lines))
        else:
            pass
    if not (api_methods and spi_methods):
        raise RuntimeError("{} not found".format("api" if api_methods is None else "spi"))
    return api_methods, spi_methods


class PyCodeGenerator(object):
    def __init__(self, api_path):
        self._types: OrderedDict[str, Union[CustomType, EnumType]] = OrderedDict()
        self._structs = OrderedDict()
        self._trader_api_methods = None
        self._trader_spi_methods = None
        self._md_api_methods = None
        self._md_spi_methods = None

        with open(os.path.join(api_path, "ThostFtdcUserApiDataType.h"), encoding="GBK") as f:
            for type_obj in parse_data_type_header(f.readlines()):
                self._types[type_obj.name] = type_obj

        with open(os.path.join(api_path, "ThostFtdcUserApiStruct.h"), encoding="GBK") as f:
            for struct_obj in parse_struct_header(f.readlines(), self._types):
                self._structs[struct_obj.name] = struct_obj

        with open(os.path.join(api_path, "ThostFtdcTraderApi.h"), encoding="GBK") as f:
            self._trader_api_methods, self._trader_spi_methods = parse_api_header(f.readlines(), self._structs)

        with open(os.path.join(api_path, "ThostFtdcMdApi.h"), encoding="GBK") as f:
            self._md_api_methods, self._md_spi_methods = parse_api_header(f.readlines(), self._structs)

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

        for trader_md, api_methods, spi_methods in [
            ("Trader", self._trader_api_methods, self._trader_spi_methods),
            ("Md", self._md_api_methods, self._md_spi_methods),
        ]:
            with open(os.path.join(py_path, f"ThostFtdc{trader_md}Api.pxd"), "w+", encoding="utf-8") as f:
                template = env.get_template(f"ThostFtdcApi.pxd.jinja")
                f.write(template.render(methods=api_methods, trader_md=trader_md))

            with open(os.path.join(py_path, f"{trader_md}Api.pyx"), "w+", encoding="utf-8") as f:
                template = env.get_template("Api.pyx.jinja")
                f.write(template.render(api_methods=api_methods, spi_methods=spi_methods, trader_md=trader_md))


if __name__ == "__main__":
    PyCodeGenerator("ctp").write("rqctp")
