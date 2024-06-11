# I am having issues running the tests,
# specifically with their errors. I will ask about it on Q&A.
from __future__ import annotations
import sys
import os
from datetime import datetime


def make_directory(directories: list) -> str | bytes:
    directory_part = os.path.join(*directories)
    os.makedirs(directory_part, exist_ok=True)
    return directory_part


def make_files(file_name: str | list[str], path: str = ".") -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %I:%M:%S") + "\n")
        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


def main() -> None:
    sys_input = sys.argv
    if "-f" in sys_input:
        make_files(sys_input[-1])
    if "-d" in sys_input:
        make_files(sys_input[2:])
    if "-f" in sys_input and "-d" in sys_input:
        make_files(sys_input[-1], make_directory(sys_input[2: -2]))


if __name__ == "__main__":
    main()
