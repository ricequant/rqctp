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

from ctypes import Structure
from collections import namedtuple


def process_field(value):
    if isinstance(value, bytes):
        try:
            return value.decode("GBK")
        except UnicodeDecodeError:
            pass
    return value


class Struct(Structure):
    _tuple_type = None

    @classmethod
    def get_tuple_type(cls):
        if cls._tuple_type is None:
            cls._tuple_type = namedtuple(cls.__name__, (f for f, _ in cls._fields_))
        return cls._tuple_type

    def to_tuple(self):
        return self.get_tuple_type()(*[process_field(getattr(self, f)) for f, _ in self._fields_])


def as_struct(cls):
    print(", ".join("(\"{}\". {})".format(name, type_) for name, type_ in cls.__annotations__.items()))

    cls_lines = [
        f"class {cls.__name__}(Structure):",
        " " * 4 + "_field_ = [{}]".format(
            ", ".join("(\"{}\". {})".format(name, type_.__name__) for name, type_ in cls.__annotations__.items())
        )
    ]
    cls_line = "\n".join(cls_lines)
    print(cls_line)
    print("\n")
    return cls
