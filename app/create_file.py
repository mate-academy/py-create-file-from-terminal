import os
import sys
from datetime import datetime
from typing import List


def create_directories(path_parts: List[str]) -> str:
    if not path_parts:
        raise ValueError("No directory path provided.")

    path = os.path.join(*path_parts)

    if not os.path.exists(path):
        os.makedirs(path)
        print(f'Directory {"/".join(path_parts)} created.')
    return path


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_content() -> List[str]:
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(filepath: str, content_lines: List[str]) -> None:
    timestamp = get_timestamp()

    if os.path.exists(filepath):
        mode = "a"
    else:
        mode = "w"

    with open(filepath, mode) as f:
        if mode == "a":
            f.write("\n\n")
        f.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"Content successfully written to {filepath}")


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        while dir_index < len(args) and not args[dir_index].startswith("-"):
            directory_parts.append(args[dir_index])
            dir_index += 1

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]

    if directory_parts and file_name:
        directory_path = create_directories(directory_parts)
        filepath = os.path.join(directory_path, file_name)
    elif file_name:
        filepath = os.path.join(os.getcwd(), file_name)
    else:
        print("Usage: python create_file.py [-d directory] [-f filename]")
        return

    content_lines = get_content()
    write_to_file(filepath, content_lines)


if __name__ == "__main__":
    main()
