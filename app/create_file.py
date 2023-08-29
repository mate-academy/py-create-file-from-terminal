import sys
import os
from datetime import datetime
from typing import List


def get_lines() -> List[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def create_file(file_name: str) -> None:
    if not os.path.exists(file_name):
        open(file_name, "a").close()


def write_file(file_name: str) -> None:
    lines = get_lines()
    with open(file_name, "a") as file:
        if os.path.getsize(file_name) != 0:
            file.write("\n")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now}\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")


def get_path(directories: List[str]) -> str:
    current_dir = os.getcwd()
    path = os.path.join(current_dir, *directories)
    return path


def main(arguments: List[str]) -> None:
    if "-d" in arguments and "-f" not in arguments:
        directories = arguments[arguments.index("-d") + 1 :]
        path = get_path(directories)
        if not os.path.exists(path):
            os.makedirs(path)
        return

    if "-f" in arguments and "-d" not in arguments:
        file_name = arguments[arguments.index("-f") + 1]
        create_file(file_name)
        write_file(file_name)
        return

    directories = arguments[arguments.index("-d") + 1 : arguments.index("-f")]
    file_name = arguments[arguments.index("-f") + 1]
    path = get_path(directories)
    if not os.path.exists(path):
        os.makedirs(path)
    full_path = os.path.join(path, file_name)
    create_file(full_path)
    write_file(full_path)


if __name__ == "__main__":
    main(sys.argv)
