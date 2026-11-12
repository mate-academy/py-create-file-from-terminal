from __future__ import annotations

import os
import sys
from datetime import datetime


def create_file() -> None:
    arguments = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in arguments:
        directory_index = arguments.index("-d")
        file_index = (
            arguments.index("-f")
            if "-f" in arguments
            else len(arguments)
        )
        directories = arguments[directory_index + 1:file_index]

    if "-f" in arguments:
        file_index = arguments.index("-f")
        file_name = arguments[file_index + 1]

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{number} {line}"
        for number, line in enumerate(content_lines, start=1)
    ]
    new_content = "\n".join([timestamp, *numbered_lines])

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n\n")
            file.write(new_content)
    else:
        with open(file_path, "w") as file:
            file.write(new_content)


if __name__ == "__main__":
    create_file()
