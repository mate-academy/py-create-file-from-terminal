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


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        if d_index + 1 >= len(args) or args[d_index + 1].startswith("-"):
            print("Error: No directories specified after -d")
            return
        dirs = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args) or args[f_index + 1].startswith("-"):
            print("Error: No file name specified after -f")
            return
        file_name = args[f_index + 1]

        if "-d" not in args or f_index < d_index:
            path = os.path.join(*dirs) if dirs else ""
            file_path = os.path.join(path, file_name) if path else file_name
            create_file(file_path)
        else:
            path = os.path.join(*dirs)
            create_directories(path)
            file_path = os.path.join(path, file_name)
            create_file(file_path)
    elif "-d" in args:
        path = os.path.join(*dirs)
        create_directories(path)


if __name__ == "__main__":
    main()
