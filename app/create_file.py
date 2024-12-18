import os
import sys
from datetime import datetime
from typing import TextIO
from xmlrpc.client import DateTime


def create_directory(path_parts) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_or_append_file(file_path) -> TextIO:
    return open(file_path, "a")


def main():
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else None
        path_parts = args[d_index + 1: f_index] if f_index else args[d_index + 1:]
        directory = create_directory(path_parts)
    else:
        directory = "."

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = os.path.join(directory, file_name)

        with create_or_append_file(file_path) as file:
            timestamp = get_timestamp()
            file.write(f"\n{timestamp}\n")
            line_number = 1

            while True:
                content = input(f"Enter content line ({line_number}): ")
                if content.strip().lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1


if __name__ == "__main__":
    main()