import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

version = '0.1'

setup(
    name='tx4877',
    version=version,
    description="",
    author='Emile Caron and J\xc3\xa9r\xc3\xa9my Co Kim Len',
    install_requires=[
          "PyQt4",
    ],
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)],
)
