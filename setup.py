from cx_Freeze import setup, Executable
base = None

executables = [Executable("v3.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)