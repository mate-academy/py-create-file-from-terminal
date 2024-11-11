import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(path: str) -> None:
    append_content = "a" if os.path.exists(path) else "w"

    with open(path, append_content) as f:
        timemark = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timemark}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def menu() -> None:
    args = sys.argv[1:]
    dir_path = None
    file_name = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        end_index = args.index("-f") if "-f" in args else len(args)
        dir_path = os.path.join(*args[dir_index:end_index])
        create_directory(dir_path)

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(dir_path if dir_path else ".", file_name)
        create_file(file_path)


if __name__ == "__main__":
    menu()
