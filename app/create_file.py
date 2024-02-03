import os
import sys
from datetime import datetime


def create_file(
        directory: str,
        file_name: str,
        content_lines: list
) -> None:
    file_path = os.path.join(directory, file_name)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{datetime_now}\n"]

    for i, line in enumerate(content_lines, start=1):
        content.append(f"{i} {line}\n")

    with open(file_path, "a" if os.path.exists(file_path) else "w") as file:
        file.writelines(content)


def main() -> None:
    args = sys.argv[1:]

    directory = ""
    file_name = ""

    if "-d" in args:
        dir_index = args.index("-d")
        directory_args = args[dir_index + 1:]
        if "-f" in args:
            file_index = args.index("-f")
            if file_index > dir_index:
                directory_args = args[dir_index + 1:file_index]
                file_name = args[file_index + 1]

        directory = os.path.join(*directory_args)
        os.makedirs(directory, exist_ok=True)

    if "-f" in args and not file_name:
        file_index = args.index("-f")
        file_name = args[file_index + 1]

    if file_name:
        content_lines = []
        print("Enter content lines (type 'stop' to finish):")

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        create_file(directory, file_name, content_lines)
