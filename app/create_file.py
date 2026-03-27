import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(path_parts: List[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_or_append_file(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dir1 dir2 ...] -f filename")
        return

    dir_path: List[str] = []
    file_name: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    full_dir_path = create_directory(dir_path) if dir_path else os.getcwd()

    if file_name:
        file_path = os.path.join(full_dir_path, file_name)
        create_or_append_file(file_path)
    else:
        print("No filename provided. Directory created if specified.")


if __name__ == "__main__":
    main()
