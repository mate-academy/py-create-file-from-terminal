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
        with open(file_name, "a") as output_file:
            time_now = datetime.now()
            output_file.write(time_now.strftime("2022-02-01 14:41:10 \n"))
            for line in file_content:
                output_file.write(line + "\n")


def create_file() -> None:
    args = sys.argv
    if "-f" in args and "-d" in args:
        if args.index("-d") < args.index("-f"):
            directories = args[args.index("-d")
                               + 1: args.index("-f")]
            filename = args[args.index("-f") + 1]
        else:
            directories = args[args.index("-d") + 1:]
            filename = args[args.index("-f") + 1]
        file_name = os.path.join(create_directory(directories), filename)
        file_creator(file_name)
    elif "-f" in args:
        filename = args[args.index("-f") + 1]
        file_creator(filename)
    elif "-d" in args:
        directories = args[args.index("-d") + 1:]
        create_directory(directories)


if __name__ == "__main__":
    create_file()
