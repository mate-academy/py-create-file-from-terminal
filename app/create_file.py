import os
import sys
from datetime import datetime
from typing import Any


def create_directory(d_part: list) -> str:
    directory = os.path.join(os.getcwd(), "app", *d_part)
    os.makedirs(directory, exist_ok=True)
    return directory


def create_file(path: str, content: Any) -> None:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [f"{time}"]
    for i, line in enumerate(content):
        lines.append(f"{i + 1} {line}")

    if os.path.exists(path):
        with open(path, "a") as file:
            file.write("\n" + "\n".join(lines) + "\n")
    else:
        with open(path, "w") as file:
            file.write("\n".join(lines) + "\n")


args = sys.argv[1:]

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        d_part = args[d_index + 1:f_index]
    else:
        d_part = args[d_index + 1:]

    directory = create_directory(d_part)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    if "-d" in args:
        path = os.path.join(directory, file_name)
    else:
        path = os.path.join(os.getcwd(), "app", file_name)

    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(path, content)
