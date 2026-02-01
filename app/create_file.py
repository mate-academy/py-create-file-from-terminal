import sys
import os
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> None:
    """
    Create directories recursively based on path_parts list.
    """
    if path_parts:
        path = os.path.join(*path_parts)
        os.makedirs(path, exist_ok=True)


def create_file(file_name: str) -> None:
    """
    Create or append content to a file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content: List[str] = []

    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            content = f.readlines()

    print("Enter content lines (enter 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content.append(line.strip())

    with open(file_name, "w") as f:
        f.write(f"{timestamp}\n")
        for idx, line in enumerate(content, start=1):
            f.write(f"{idx} {line}\n")


def main() -> None:
    args: List[str] = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index: int = args.index("-d")
        file_index: int = args.index("-f")

        directory_parts: List[str] = args[dir_index + 1:file_index]
        file_name: str = args[file_index + 1]

        create_directory(directory_parts)
        create_file(os.path.join(*directory_parts, file_name))

    elif "-d" in args:
        dir_index: int = args.index("-d")
        directory_parts: List[str] = args[dir_index + 1:]

        create_directory(directory_parts)

    elif "-f" in args:
        file_index: int = args.index("-f")
        file_name: str = args[file_index + 1]

        create_file(file_name)

    else:
        print("Invalid arguments. "
              "Use -d for directory path or -f for file name.")


if __name__ == "__main__":
    main()
