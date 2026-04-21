# write your code here
import sys
import os
from datetime import datetime


def create_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{now}\n")
        line_number = 1
        while True:
            line = input(f"Enter content line {line_number}: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def get_files() -> list:
    args = sys.argv
    if "-f" not in args:
        return []
    start = args.index("-f") + 1
    end = len(args)
    if "-d" in args and args.index("-d") > start:
        end = args.index("-d")
    return args[start:end]


def get_dirs() -> list:
    args = sys.argv
    if "-d" not in args:
        return []
    start = args.index("-d") + 1
    end = len(args)
    if "-f" in args and args.index("-f") > start:
        end = args.index("-f")
    return args[start:end]


def main() -> None:
    files = get_files()
    if not files:
        return
    dirs = get_dirs()
    path = os.sep.join(dirs)
    create_directories(path)
    file_name = files[0]
    file_path = os.path.join(path, file_name)
    create_file(file_path)


if __name__ == "__main__":
    main()
