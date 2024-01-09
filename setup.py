from cx_Freeze import setup, Executable

assets = [
    # Images
    ("Assests/icon.png", "Assests/icon.png"),
    ("Assests/cube.png", "Assests/cube.png"),
    ("Assests/up.png", "Assests/up.png"),
    ("Assests/circle.png", "Assests/circle.png"),
    ("Assests/maroon.png", "Assests/maroon.png"),
    # Fonts
    ("Assests/fonts/font.ttf", "Assests/fonts/font.ttf"),
    # Music
    ("Assests/Music/Annis II.ogg", "Assests/Music/Annis II.ogg"),
    ("Assests/Music/One Click.ogg", "Assests/Music/One Click.ogg"),
    ("Assests/Music/Polygonal Madness.ogg", "Assests/Music/Polygonal Madness.ogg"),
    ("Assests/Music/The End.ogg", "Assests/Music/The End.ogg"),
    ("Assests/Music/This time Python!.ogg", "Assests/Music/This time Python!.ogg"),
    # SFX
    ("Assests/SFX/Crunch.wav", "Assests/SFX/Crunch.wav"),
]

setup(
    name="ACG",
    version="0.1.0",
    description="ACG made in python",
    options={"build_exe": {"include_files": assets}},
    executables=[Executable("ACG.py")]
)

# python setup.py build