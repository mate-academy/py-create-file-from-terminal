import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        end_index = args.index("-f") if "-f" in args else len(args)
        if end_index > d_index:
            directory_parts = args[d_index + 1:end_index]
        else:
            directory_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return directory_parts, file_name


def get_content_from_user() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [timestamp]
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1

    return "\n".join(lines)


def create_directory(directory_parts: list) -> str:
    directory_parts = os.path.join(*directory_parts)
    os.makedirs(directory_parts, exist_ok=True)
    return directory_parts


def write_file(file_path: str, content: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n\n" + content)
    else:
        with open(file_path, "w") as file:
            file.write(content)


def main() -> None:
    args = sys.argv[1:]
    directory_parts, file_name = parse_args(args)

    directory_path = "."

    if directory_parts:
        directory_path = create_directory(directory_parts)

    if file_name:
        content = get_content_from_user()
        file_path = os.path.join(directory_path, file_name)
        write_file(file_path, content)


main()
