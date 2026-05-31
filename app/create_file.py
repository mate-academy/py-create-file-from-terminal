import os
import sys
from datetime import datetime


def parse_arguments(args: list[str]) -> tuple[str, str]:
    directories = []
    file_name = ""

    index = 0
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and args[index] != "-f":
                directories.append(args[index])
                index += 1
        elif args[index] == "-f":
            file_name = args[index + 1]
            index += 2
        else:
            index += 1

    return os.path.join(*directories) if directories else "", file_name


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_file(file_path: str, lines: list[str]) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for index, line in enumerate(lines, start=1):
            file.write(f"\n{index} {line}")


def main() -> None:
    directory_path, file_name = parse_arguments(sys.argv[1:])

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        lines = get_content()
        write_file(file_path, lines)


main()
