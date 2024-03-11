# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup,find_packages
import subprocess

__version__ = "0.0.2"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    # annotate this part if eigen version higher than 3.3.7
    Pybind11Extension(
        "px4Controller.traj_tools.polyTrajGen",
        ["bind/polyTrajGen.cpp","src/polynomial_traj.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include","/usr/include/eigen3"],

    ),

    
    Pybind11Extension(
        "pyControl",
        ["bind/pyControl.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include","/usr/include/eigen3"],
    ),
    Pybind11Extension(
        "pyParallelControl",
        ["bind/pyParallelControl.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=["include","/usr/include/eigen3"],

    ),
]

setup(
    name="px4Controller",
    version=__version__,
    author="Wang Hao",
    author_email="hwangwork@163.com",
    url="https://github.com/pybind/python_example",
    description="Px4 Quadrotor Contorller",
    long_description="",
    packages=find_packages(),
    install_requires=[
        # 列出项目的依赖项
        # 'torch',
    ],
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
