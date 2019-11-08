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
