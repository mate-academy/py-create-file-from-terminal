import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


args = sys.argv[1:]

directory = ""
file_name = ""

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1:f_index]
    else:
        directories = args[d_index + 1:]

    if directories:
        directory = os.path.join(*directories)
        os.makedirs(directory, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")

    if f_index + 1 < len(args):
        file_name = args[f_index + 1]

if file_name:
    file_path = (
        os.path.join(directory, file_name)
        if directory
        else file_name
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = get_content()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n\n")

        file.write(f"{timestamp}\n")

        for index, line in enumerate(content_lines, start=1):
            file.write(f"{index} {line}\n")
