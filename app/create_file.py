import sys
import os
from datetime import datetime


def create_directory(directories: list[str]) -> str:
    path = os.getcwd()
    for directory in directories:
        path = os.path.join(path, directory)
    os.makedirs(path, exist_ok=True)
    return path


def file_creator(file_name: str) -> None:
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
            f.write(time_now.strftime("%m-%d-%Y %H-%M-%S\n"))
            for line in file_content:
                f.write(line + "\n")


def create_file() -> None:
    args = sys.argv
    if "-f" in args and "-d" in args:
        if args.index("-d") < args.index("-f"):
            directories = args[args.index("-d")
                               + 1: args.index("-f")]
            file = args[args.index("-f") + 1]
        else:
            directories = args[args.index("-d") + 1:]
            file = args[args.index("-f") + 1]
        file_name = os.path.join(create_directory(directories), file)
        file_creator(file_name)
    elif "-f" in args:
        file = args[args.index("-f") + 1]
        file_creator(file)
    elif "-d" in args:
        directories = args[args.index("-d") + 1:]
        create_directory(directories)


if __name__ == "__main__":
    create_file()
