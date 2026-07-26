import sys
import os
from datetime import datetime
from typing import List


def create_directories(path_parts: List[str]) -> str:
    directory_path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(file_path: str) -> None:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n{time_now}\n")
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.strip().lower() == "stop":
                break
            f.write(f"{line_number} {user_input}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dirs] -f [filename]")
        return

    dir_parts = []
    file_name = None
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            return

    target_directory = os.getcwd()
    if dir_parts:
        target_directory = create_directories(dir_parts)

    if file_name:
        file_path = os.path.join(target_directory, file_name)
        create_file(file_path)
        print(f"File saved at: {file_path}")
    elif dir_parts:
        print(f"Directory created at: {target_directory}")


if __name__ == "__main__":
    main()
