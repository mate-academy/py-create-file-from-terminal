import os
import sys
from datetime import datetime


def make_dir(arguments: list[str]) -> os.path:
    joined_path = ""
    if "-d" in arguments:
        path = []
        for argument in arguments[2:]:
            if argument == "-f":
                break
            path.append(argument)
        joined_path = os.path.join(*path)
        if not os.path.exists(joined_path):
            os.makedirs(joined_path)
    return joined_path


def file_name(arguments: list[str]) -> str:
    if "-f" in arguments:
        return arguments[-1]
    return ""


def datetime_string() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"


def content_manager(path: os.path, name: str) -> None:
    with open(os.path.join(path, name), "a") as file:
        file.write(datetime_string())
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1
        file.write("\n")


def main() -> None:
    arguments = sys.argv
    name = file_name(arguments)
    path = make_dir(arguments)
    if name:
        content_manager(path, name)


if __name__ == "__main__":
    main()
