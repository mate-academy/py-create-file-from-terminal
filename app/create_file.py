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
    if "-d" in argv and "-f" in argv:
        create_path(path.sep.join(
            argv[argv.index("-d") + 1:argv.index("-f")]), argv[-1]
        )
    elif "-d" in argv:
        create_dirs(path.sep.join(argv[argv.index("-d") + 1:]))
    elif "-f" in argv:
        create_path(path.curdir, argv[-1])
