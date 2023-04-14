import datetime
from sys import argv
from os import makedirs, path
from pathlib import Path


def create_dirs(file_path: str) -> None:
    makedirs(file_path, exist_ok=True)


def create_path(file_path: str, file_name: str) -> None:
    create_dirs(file_path)

    file_path = Path(file_path) / file_name
    with file_path.open("a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        for count, input_string in enumerate(iter(input, "stop")):
            file.write(f"{count} {input_string}\n")


def create_file() -> None:
    if "-f" in argv:
        file_index = argv.index("-f")
        file_name = argv[file_index + 1]
        dir_index = None
        for i, x in enumerate(argv):
            if x == "-d" and i < file_index:
                dir_index = i

        if dir_index is not None:
            dir_path = path.sep.join(argv[dir_index + 1:file_index])
        else:
            dir_path = path.curdir

        create_path(dir_path, file_name)
    elif "-d" in argv:
        create_dirs(path.sep.join(argv[argv.index("-d") + 1:]))
