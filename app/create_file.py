import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
    print(f"File '{file_path}' created/updated successfully.")


def parse_arguments() -> None:
    args = sys.argv[1:]

    if not args:
        print("Use: python create_file.py -d dir1 dir2 [-f filename.txt]")
        return

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        path_parts = args[d_index + 1:f_index]
        file_name = args[f_index + 1]

    elif "-d" in args:
        d_index = args.index("-d")
        path_parts = args[d_index + 1:]
        file_name = None

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        path_parts = []

    else:
        print("Use: python create_file.py -d dir1 dir2 -f filename.txt")
        return

    path = os.path.join(*path_parts)

    if path_parts:
        create_directory(path)

    if file_name:
        file_path = os.path.join(str(path), file_name) if path else file_name
        create_file(file_path)


if __name__ == "__main__":
    parse_arguments()
