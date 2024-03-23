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
            + "\n"
        )
        while True:
            content_line = input("Enter content line:")
            if content_line == "stop":
                file.write("\n")
                break
            string_number = 1
            file.write(str(string_number)
                       + " "
                       + content_line
                       + "\n")
            string_number += 1


if __name__ == "__main__":
    files = []

    if "-d" in sys.argv:
        for element in sys.argv[sys.argv.index("-d") + 1:]:
            if element == "-f":
                break

            files.append(element)
        create_path(files)

        if "-f" in sys.argv:
            file_path = files + [
                sys.argv[sys.argv.index("-f") + 1]
            ]

            add_content_to_file(file_path)
