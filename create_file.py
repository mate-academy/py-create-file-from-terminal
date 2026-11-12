from __future__ import annotations

import argparse
import os
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="*",
        default=[],
        help="Directory names",
    )
    parser.add_argument(
        "-f",
        help="File name",
    )
    arguments = parser.parse_args()

    if arguments.d:
        directory_path = os.path.join(*arguments.d)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if arguments.f is None:
        return

    file_path = os.path.join(directory_path, arguments.f)
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
