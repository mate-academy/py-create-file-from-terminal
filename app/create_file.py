import sys
import os
from datetime import datetime


def parse_args(args: list) -> tuple:
    directories = []
    filename = None

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        # suporta qualquer ordem: -d antes ou depois de -f
        if d_index < f_index:
            directories = args[d_index + 1:f_index]
            filename = args[f_index + 1]
        else:
            filename = args[f_index + 1]
            directories = args[d_index + 1:]

    elif "-d" in args:
        directories = args[args.index("-d") + 1:]

    elif "-f" in args:
        filename = args[args.index("-f") + 1]

    return directories, filename


def create_directory(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def collect_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(filepath: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(filepath)

    with open(filepath, "a") as source_file:
        if file_exists:
            source_file.write("\n")
        source_file.write(f"{timestamp}\n")
        for number, content in enumerate(lines, start=1):
            source_file.write(f"{number} {content}\n")


def main() -> None:
    args = sys.argv[1:]
    directories, filename = parse_args(args)

    path = "."
    if directories:
        path = create_directory(directories)

    if filename:
        filepath = os.path.join(path, filename)
        lines = collect_content()
        write_to_file(filepath, lines)


main()
