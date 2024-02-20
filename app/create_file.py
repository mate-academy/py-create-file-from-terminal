import sys
import os
from datetime import datetime


def parse_arguments(args: list[str]) -> tuple[list[str], str]:
    d_path, f_file = [], ""
    if "-d" in args and "-f" in args:
        d_path = args[args.index("-d") + 1:args.index("-f")]

    if "-d" in args and not d_path:
        d_path = args[args.index("-d") + 1:]

    if "-f" in args:
        f_file = args[args.index("-f") + 1]
    return d_path, f_file


def create_dirs(d_path: list[str]) -> None:
    full_path = os.path.join(*d_path)
    os.makedirs(full_path, exist_ok=True)


def create_file(d_path: list[str], f_file: str) -> None:
    full_path = os.path.join(*d_path, f_file)

    content_lines = []
    while True:
        text_line = input("Enter content line: ")
        if text_line.lower() == "stop":
            break
        content_lines.append(text_line)

    with open(full_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        for line_number, line in enumerate(content_lines, start=1):
            file.write(f"{line_number} {line}\n")
        file.write("\n")


if __name__ == "__main__":
    arguments = sys.argv
    path_list, file_name = parse_arguments(arguments)

    if path_list:
        create_dirs(path_list)

    if file_name:
        create_file(path_list, file_name)
