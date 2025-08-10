import sys
import os
from datetime import datetime
from typing import List


def create_dir(path_parts: List[str]) -> None:
    if path_parts:
        os.makedirs("/".join(path_parts), exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        user_input = input("Enter content line: ")
        while user_input != "stop":
            f.write(f"{count} {user_input}\n")
            count += 1
            user_input = input("Enter content line: ")


def main() -> None:
    args = sys.argv
    if len(args) < 3:
        print("Error: Not enough arguments provided.")
        print("Usage examples:")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2")
        sys.exit(1)

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index > f_index:
            print("Error: -d must come before -f")
            sys.exit(1)

        dir_parts = args[d_index + 1:f_index]
        if not dir_parts:
            print("Error: No directory names provided after -d")
            sys.exit(1)

        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: No file name provided after -f")
            sys.exit(1)

        create_dir(dir_parts)
        file_path = "/".join(dir_parts + [file_name])
        create_file(file_path)

    elif "-d" in args:
        d_index = args.index("-d")
        dir_parts = args[d_index + 1:]
        if not dir_parts:
            print("Error: No directory names provided after -d")
            sys.exit(1)
        create_dir(dir_parts)

    elif "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: No file name provided after -f")
            sys.exit(1)
        create_file(file_name)
    else:
        print("Error: No -d or -f flags found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
