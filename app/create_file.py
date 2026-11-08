import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    already_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if already_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    current_flag = None

    for arg in args:
        if arg in ("-d", "-f"):
            current_flag = arg
        elif current_flag == "-d":
            directories.append(arg)
        elif current_flag == "-f" and file_name is None:
            file_name = arg

    return directories, file_name


def main() -> None:
    directories, file_name = parse_args(sys.argv[1:])
    path = os.path.join(*directories) if directories else ""

    if path:
        os.makedirs(path, exist_ok=True)

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
        write_file(file_path, get_content())


main()
