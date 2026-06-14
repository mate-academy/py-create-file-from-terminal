import sys
import os
from datetime import datetime


def parse_args(argv: list) -> tuple:
    directories = []
    file_name = ""
    current_mode = None

    for arg in argv[1:]:
        if arg == "-d":
            current_mode = "dir"
        elif arg == "-f":
            current_mode = "file"
        else:
            if current_mode == "dir":
                directories.append(arg)
            elif current_mode == "file" and not file_name:
                file_name = arg

    return directories, file_name


def create_directory(directories: list) -> None:
    if directories:
        folder_path = os.path.join(*directories)
        os.makedirs(folder_path, exist_ok=True)


def collect_content_lines() -> list:
    content_lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(f"{line_number} {line}\n")
        line_number += 1
    return content_lines


def write_content(directories: list, file_name: str,
                  content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_path = os.path.join(*directories, file_name)\
        if directories else file_name

    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        with open(full_path, "a") as file:
            file.write("\n")

    with open(full_path, "a") as file:
        file.write(f"{timestamp}\n")
        file.writelines(content_lines)


def main() -> None:
    directories, file_name = parse_args(sys.argv)
    create_directory(directories)
    if file_name:
        content_lines = collect_content_lines()
        write_content(directories, file_name, content_lines)


if __name__ in ("__main__", "<run_path>"):
    main()
