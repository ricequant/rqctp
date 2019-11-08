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
import shutil
from distutils.core import setup

from Cython.Build import cythonize
from Cython.Distutils import Extension

project_dir = os.path.dirname(os.path.abspath(__file__))
ctp_dir = os.path.join(project_dir, "rqctp")
lib_dir = os.path.join(project_dir, "ctp")

for name in os.listdir(ctp_dir):
    if name.endswith(".so") or name.endswith(".cpp"):
        os.remove(os.path.join(ctp_dir, name))

for name in os.listdir(lib_dir):
    if name.endswith(".so") or name.endswith(".h"):
        shutil.copy(os.path.join(lib_dir, name), os.path.join(ctp_dir, name))

setup(
    name="rqctp",
    version="0.0.1",
    ext_modules=cythonize(module_list=[
        Extension(
            name="rqctp.TraderApi",
            sources=["rqctp/TraderApi.pyx"],
            libraries=["thosttraderapi_se"],
            language="c++",
            library_dirs=["rqctp/"],
            extra_link_args=['-Wl,-rpath,$ORIGIN'],
        )
    ], compiler_directives={
        "language_level": 3,
        "binding": True
    }),
    requires=[
        "Cython"
    ]
)
