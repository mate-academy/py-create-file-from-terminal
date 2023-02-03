import sys
import os
from datetime import datetime


def get_command() -> list:
    return sys.argv[1:]


def get_file_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        time = datetime.now()
        file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\n")
    line_counter = 0
    while True:
        line_counter += 1
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        line_content = f"{line_counter} {content_line}\n"
        with open(file_path, "a") as file:
            file.write(line_content)
    with open(file_path, "a") as file:
        file.write("\n")


def create_file() -> None:
    command = get_command()
    if "-f" not in command:
        directories = ["app"] + command[1:]
        path = os.path.join(*directories)
        os.makedirs(path)
    else:
        if command[0] == "-d":
            directories = ["app"] + command[1:-2]
            path = os.path.join(*directories)
            os.makedirs(path)
            file_path = os.path.join(path, command[-1])
        else:
            file_path = os.path.join("app", command[-1])
        get_file_content(file_path)


create_file()
