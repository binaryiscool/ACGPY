from cx_Freeze import setup, Executable

assets = [
    ("Assests/icon.png", "Assests/icon.png"),
    ("Assests/cube.png", "Assests/cube.png"),
    ("Assests/font.ttf", "Assests/font.ttf"),
]

setup(
    name="ACG",
    version="0.1.0",
    description="ACG made in python",
    options={"build_exe": {"include_files": assets}},
    executables=[Executable("ACG.py")]
)