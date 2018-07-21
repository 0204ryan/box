import sys
import os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


from cx_Freeze import setup, Executable

build_exe_options = {'include_files': ['piano.mp3', 'background.jpg', 'heli.png', 'wt014.ttf'], 'packages':['pygame']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = Executable('main.py', base=base, targetName='方塊戰爭.exe')

setup(
        name = "box 1.1",
        version = "1.1",
        description = "a pygame game",
        options = {'build_exe': build_exe_options},
        executables = [executable])