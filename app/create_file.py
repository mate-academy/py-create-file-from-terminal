import sys
import os
from datetime import datetime
from typing import List


def create_directories(path_parts: List[str]) -> str:
    dir_path = os.path.join(*path_parts)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Directory created: {dir_path}")
    else:
        print(f"Directory already exists: {dir_path}")
    return dir_path


def create_or_append_file(file_path: str) -> None:
    append = os.path.exists(file_path)

    if append:
        print(f"File '{file_path}' exists. Appending new content.")
    else:
        print(f"Creating new file: {file_path}")

    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1

        print(f"Content written to {file_path}")


def main() -> None:
    args = sys.argv
    dir_path = os.getcwd()

    if "-d" in args:
        dir_index = args.index("-d") + 1
        dirs = []
        while (dir_index < len(args) and args[dir_index] != "-f"):
            dirs.append(args[dir_index])
            dir_index += 1
        if dirs:
            dir_path = create_directories(dirs)

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]
            file_path = os.path.join(dir_path, file_name)
            create_or_append_file(file_path)
        else:
            print("Error: No file name provided after '-f' flag.")
    else:
        print("Error: No '-f' flag for file creation found.")


if __name__ == "__main__":
    main()
