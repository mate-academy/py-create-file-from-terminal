import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def get_mode(file_path: str) -> str:
    return "a" if os.path.exists(file_path) else "w"


def write_content_to_file(file_path: str) -> None:
    with open(file_path, get_mode(file_path)) as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args: list[str] = sys.argv[1:]
    dir_path = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = os.path.join(*args[d_index + 1:])
        create_directory(dir_path)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = (
            os.path.join(dir_path, file_name)
            if dir_path
            else file_name
        )
        write_content_to_file(file_path)
