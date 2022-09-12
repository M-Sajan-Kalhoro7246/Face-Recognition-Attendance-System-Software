import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="faceicon.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Attendence Software",
    options = {"build_exe": {"packages":["tkinter","os","sys"], "include_files":["faceicon.ico",'tcl86t.dll','tk86t.dll', 'Images','data_img','databaseTest','Attendence_Data']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace Management System | Developed By MUHAMMAD_SAJAN_KALHORO",
    executables = executables
    )
