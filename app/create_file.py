from datetime import datetime

import sys
import os


def make_directory(dir_list: list) -> str:
    path = ""
    for directory in dir_list:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    return path


def make_file(filename: str, path: str = "") -> None:
    with open(os.path.join(path, filename), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        linestart = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            file.write(f"{linestart} {line}\n")
            linestart += 1


def processing_arguments() -> None:
    argv = sys.argv

    if "-d" in argv and "-f" in argv:
        directories = argv[argv.index("-d") + 1:]
        if "-f" in directories:
            directories = directories[:directories.index("-f")]
        filename = argv[argv.index("-f") + 1]
        path = make_directory(directories)
        make_file(filename, path)
    elif "-d" in argv:
        path = argv[argv.index("-d") + 1:]
        make_directory(path)
    elif "-f" in argv:
        filename = argv[argv.index("-f") + 1]
        make_file(filename)


if __name__ == "__main__":
    processing_arguments()
