import sys
import os
from datetime import datetime
from typing import Optional


def create_file(file_path: str) -> None:
    append_mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, append_mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")


def main() -> None:
    args = sys.argv
    directory: Optional[str] = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        directory = os.path.join(*args[dir_index:])
        create_directory(directory)

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(directory or "", file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
