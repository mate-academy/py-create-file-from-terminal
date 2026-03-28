import sys
import os
from datetime import datetime
from typing import List


def create_directories(path_list: List[str]) -> str:
    path = os.path.join(*path_list)
    os.makedirs(path, exist_ok=True)
    return path


def get_file_content() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content_lines: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = args[d_index + 1:]
        if "-f" in dir_path:
            f_index = dir_path.index("-f")
            dir_path = dir_path[:f_index]
        args = args[:d_index] + args[d_index + len(dir_path) + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        args = args[:f_index]

    if dir_path:
        directory = create_directories(dir_path)
    else:
        directory = os.getcwd()

    if file_name:
        file_path = os.path.join(directory, file_name)
        content_lines = get_file_content()
        write_to_file(file_path, content_lines)
        print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
