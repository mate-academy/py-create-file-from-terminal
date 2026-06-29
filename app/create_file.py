import os
import sys
from datetime import datetime


def get_directory(args: list[str]) -> str:
    if "-d" not in args:
        return ""

    start = args.index("-d") + 1
    directories = []

    for arg in args[start:]:
        if arg.startswith("-"):
            break
        directories.append(arg)

    if not directories:
        return ""

    return os.path.join(*directories)


def get_filename(args: list[str]) -> str | None:
    if "-f" not in args:
        return None

    index = args.index("-f") + 1

    if index >= len(args):
        return None

    return args[index]


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

    with open(file_path, "a", encoding="utf-8") as source_file:
        if file_exists:
            source_file.write("\n")

        source_file.write(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        for index, line in enumerate(lines, start=1):
            source_file.write(f"{index} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directory = get_directory(args)
    filename = get_filename(args)

    if directory:
        os.makedirs(directory, exist_ok=True)

    if filename is None:
        return

    if directory:
        file_path = os.path.join(directory, filename)
    else:
        file_path = filename

    lines = get_content()
    write_file(file_path, lines)


main()
