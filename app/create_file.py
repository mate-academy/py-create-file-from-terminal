import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    if not directories:
        return ""
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def write_content_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_blank_line = (os.path.exists(file_path)
                      and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as file:
        if add_blank_line:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for index, content in enumerate(lines, start=1):
            file.write(f"{index} {content}\n")


def main() -> None:
    args = sys.argv[1:]

    file_name = None
    dir_parts = []

    if "-d" in args:
        d_idx = args.index("-d")
        if "-f" in args and args.index("-f") > d_idx:
            dir_parts = args[d_idx + 1 : args.index("-f")]
        else:
            dir_parts = args[d_idx + 1 :]

    if "-f" in args:
        f_idx = args.index("-f")
        file_name = args[f_idx + 1]

    target_dir = create_path(dir_parts)

    if file_name:
        file_path = os.path.join(target_dir, file_name)\
            if target_dir else file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        write_content_to_file(file_path, lines)


main()
