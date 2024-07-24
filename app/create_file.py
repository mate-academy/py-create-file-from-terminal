import os
import sys
from datetime import datetime


def create_directory(directories: list[str]) -> str:
    path = os.getcwd()
    for directory in directories:
        path = os.path.join(path, directory)
    os.makedirs(path, exist_ok=True)
    return path


def file_creator(file_name: str) -> None:
    with open(file_name, "a") as f:
        pass
    file_content = []
    i = 1
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        file_content.append(f"{i} {content_line}")
        i += 1
    if file_content:
        with open(file_name, "a") as f:
            time_now = datetime.now()
            f.write(time_now.strftime("%m-%d-%Y %H:%M:%S\n"))
            for line in file_content:
                f.write(line + "\n")
            f.write("\n")


def create_file() -> None:
    if "-f" in sys.argv and "-d" in sys.argv:
        if sys.argv.index("-d") < sys.argv.index("-f"):
            directories = sys.argv[sys.argv.index("-d")
                                   + 1: sys.argv.index("-f")]
        else:
            directories = sys.argv[sys.argv.index("-d") + 1:]
        file_ = sys.argv[sys.argv.index("-f") + 1]
        file_name = os.path.join(create_directory(directories), file_)
        file_creator(file_name)
    elif "-f" in sys.argv:
        file_ = sys.argv[sys.argv.index("-f") + 1]
        file_creator(file_)
    elif "-d" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:]
        create_directory(directories)


if __name__ == "__main__":
    create_file()
