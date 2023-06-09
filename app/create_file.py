import os
import sys
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> None:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Created directory: {directory_path}")


def create_file(directory: str, file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)

    file_path = os.path.join(directory, file_name)

    with open(file_path, "a+") as file:
        file.seek(0)
        existing_content = file.read().strip()
        if existing_content:
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")

    print(f"File created: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        if dir_index < file_index:
            dir_path_parts = args[dir_index + 1:file_index]
            file_name = args[file_index + 1]
        else:
            file_name = args[file_index + 1]
            dir_path_parts = args[dir_index + 1:file_index]
        create_directory(dir_path_parts)
        create_file(os.path.join(*dir_path_parts), file_name)
    elif "-d" in args:
        dir_index = args.index("-d")
        dir_path_parts = args[dir_index + 1:]
        create_directory(dir_path_parts)
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        create_file(os.getcwd(), file_name)


if __name__ == "__main__":
    main()
