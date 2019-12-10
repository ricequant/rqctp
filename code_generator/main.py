import os
import re
from collections import OrderedDict
from typing import Iterator, Optional, NamedTuple, List


class CustomType(NamedTuple):
    base_type: str
    array_len: Optional[int]
    name: str
    comment: str


def useless(l):
    return len(l.strip().replace("/", "")) == 0


def line_gen(raw_lines):
    for l in raw_lines:
        if not useless(l):
            yield l.strip()


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


def is_type_def(line: str):
    return line.startswith("typedef ")


def parse_type_def(line: str, enum_values, comment: str):
    _, base_type, name = line.split(";")[0].split()
    try:
        (name, array_len), = re.findall(r"(.+)\[(\d+)\]", name)
    except ValueError:
        array_len = None
    return CustomType(base_type, array_len, name, comment)


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
    # return EnumType(name, items)
    return None


def parse_constant_declaration(line: str, comment: str):
    _, name, value = line.split()
    # return Constant(name, value, comment)
    return None


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
            pass
            constants.append(parse_constant_declaration(l, last_comment))
        elif is_type_def(l):
            yield parse_type_def(l, constants.copy(), comment)
            comment = None
            constants.clear()
        elif is_enum_def(l):
            pass
            yield parse_enum_def(l, lines)
        elif l == "#endif":
            break
        else:
            raise RuntimeError(f"Bad line: {l}")


class PyCodeGenerator(object):
    def __init__(self, api_path):
        self._types: OrderedDict[str, CustomType] = OrderedDict()

        with open(os.path.join(api_path, "ThostFtdcUserApiDataType.h"), encoding="GBK") as f:
            for type_obj in parse_data_type_header(f.readlines()):
                if isinstance(type_obj, CustomType):
                    self._types[type_obj.name] = type_obj

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
            f.write(template.render(type_list=self._types.values()))

if __name__ == "__main__":
    PyCodeGenerator("ctp").write("rqctp")
