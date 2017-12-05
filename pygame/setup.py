import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Nick\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Nick\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
	name="Rump Racer",
	options={"build_exe": {"packages":["pygame"],"include_files":["rumpadump.png"]}},
	executables=executables)