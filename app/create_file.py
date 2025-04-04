import sys
import os
from file import file_spawn


def file_from_terminal() -> None:
    argv = sys.argv
    dir_index = argv.index("-d") if "-d" in argv else None
    file_index = argv.index("-f") if "-f" in argv else None
    path = []

    if dir_index:
        path = argv[dir_index + 1: file_index if file_index else None]
        os.makedirs(os.path.join(*path), exist_ok=True)
    if file_index:
        file_path = os.path.join(*path, argv[file_index + 1])
        file_spawn(file_path)


file_from_terminal()
