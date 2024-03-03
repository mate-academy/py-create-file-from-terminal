import sys
import os
from datetime import datetime
from typing import List


def create_path(directories: List[str]) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def add_content_to_file(file_path: str, content_lines: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "w") as file:
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args: List[str] = sys.argv[1:]
    dir_path: str = ""
    file_name: str = ""
    content_lines: List[str] = []
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        directories = args[dir_index + 1:file_index]
        dir_path = create_path(directories)
        file_name = args[file_index + 1]
    elif "-d" in args:
        dir_index = args.index("-d")
        directories = args[dir_index + 1:]
        dir_path = create_path(directories)
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    if dir_path:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name
    add_content_to_file(file_path, content_lines)


if __name__ == "__main__":
    main()
