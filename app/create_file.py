import os
import sys
from datetime import datetime


def create_directory(args: list[str]) -> str:
    """Creates a directory from the path specified after -d"""
    parent_dir = os.getcwd()
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        dir_parts = args[d_index + 1:f_index]
    else:
        dir_parts = args[d_index + 1:]
    path = os.path.join(parent_dir, *dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(args: list[str], base_path: str) -> None:
    """Creates or appends to a file in the specified path"""
    f_index = args.index("-f")
    filename = args[f_index + 1]
    file_path = os.path.join(base_path, filename) if "-d" in args else filename

    with open(file_path, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            f.write(f"{count} {line}\n")
            count += 1
        f.write("\n")
    print(f"File '{file_path}' updated.")


def main() -> None:
    args = sys.argv

    if "-d" in args and "-f" in args:
        path = create_directory(args)
        create_file(args, path)
    elif "-d" in args:
        create_directory(args)
    elif "-f" in args:
        create_file(args, os.getcwd())
    else:
        print("Please provide at least -d (directory) or -f (file).")


if __name__ == "__main__":
    main()
