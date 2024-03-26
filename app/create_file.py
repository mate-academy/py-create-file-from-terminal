import sys
import os
import datetime
from typing import List


def create_path(directories: List[str]) -> None:
    os.makedirs(os.path.join(*directories), exist_ok=True)


def add_content_to_file(file_path: str) -> None:
    with open(os.path.join(*file_path), "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        string_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                if string_number > 1:
                    file.write("\n")
                break
            file.write(f"{str(string_number)} {content_line}\n")
            string_number += 1


if __name__ == "__main__":
    files = []
    file_name = ""

    if "-d" in sys.argv:
        index = sys.argv.index("-d") + 1
        while index < len(sys.argv) and not sys.argv[index].startswith("-"):
            files.append(sys.argv[index])
            index += 1

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
    elif len(sys.argv) > 1:
        file_name = sys.argv[1]

    if files:
        create_path(files)

    if file_name:
        file_path = os.path.join(*(files + [file_name]))
        add_content_to_file(file_path)
