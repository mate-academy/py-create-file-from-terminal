import sys
import os
from datetime import datetime


def get_content_lines() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content_lines: list) -> None:
    is_existing_file = os.path.exists(file_path)

    with open(file_path, "a") as target_file:
        if is_existing_file:
            target_file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target_file.write(f"{timestamp}\n")

        line_number = 1
        for line in content_lines:
            target_file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    directories = []
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if d_index < f_index:
                directories = args[d_index + 1: f_index]
            else:
                directories = args[d_index + 1:]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        content_lines = get_content_lines()
        write_to_file(file_path, content_lines)


main()
