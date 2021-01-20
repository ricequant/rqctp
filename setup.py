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
import sys
import shutil
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize


project_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.join(project_dir, "rqctp")
lib_dir = os.path.join(project_dir, "ctp")
platform = sys.platform


if platform in ("linux", "win32"):
    if platform == "linux":
        lib_extensions = (".so", ".h")
        extra_compile_args = None
        extra_link_args = ['-Wl,-rpath,$ORIGIN']
        package_data = {"rqctp": ["libthosttraderapi_se.so"]}
    elif platform == 'win32':
        lib_extensions = (".dll", ".lib", ".h")
        extra_compile_args = ["/GR", "/EHsc"]
        extra_link_args = None
        package_data = {"rqctp": ["thosttraderapi_se.dll", "thosttraderapi_se.lib"]}

    for name in os.listdir(lib_dir):
        if any([name.endswith(e) for e in lib_extensions]):
            shutil.copy(os.path.join(lib_dir, name), os.path.join(proj_dir, name))

    ext_modules = cythonize(module_list=[
        Extension(
            name="rqctp.TraderApi",
            sources=["rqctp/TraderApi.pyx"],
            libraries=["thosttraderapi_se"],
            language="c++",
            library_dirs=["rqctp/"],
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
        )
    ], compiler_directives={
        "language_level": 3,
        "binding": True
    })

else:
    ext_modules = []
    package_data = {}

print(package_data)
setup(
    name="rqctp",
    version="0.0.2",
    ext_modules=ext_modules,
    packages=find_packages(exclude=[]),
    package_data=package_data
)
