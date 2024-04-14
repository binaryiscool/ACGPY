from cx_Freeze import setup, Executable

#Include any files or directories by adding them to this list.
includefiles = ['Assets/']  #Include Folders
build_exe_options = {
    "include_files": includefiles,
}

setup(
    name="A Click Gaem",
    version="0.0.1",
    description="A recreation of A Clicker Gaem made in python using pygame-ce & ect",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]  # Replace "main.py" with your main script
)
