import sys
import os
from datetime import datetime


def parse_arguments() -> tuple:
    directories = []
    filename = None

    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
            else:
                i += 1

        elif args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1

        else:
            i += 1

    return directories, filename


def create_directories(directories: list) -> list:
    if not directories:
        return ""
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_file_content() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exist = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as f:
        if file_exist:
            f.write("\n")
        f.write(timestamp + "\n")
        for index, line in enumerate(content_lines, 1):
            f.write(f"{index} {line}\n")


def main() -> None:
    directories, filename = parse_arguments()
    dir_path = create_directories(directories)
    if not filename:
        return
    if dir_path:
        file_path = os.path.join(dir_path, filename)
    else:
        file_path = filename

    lines = get_file_content()
    write_to_file(file_path, lines)


main()
