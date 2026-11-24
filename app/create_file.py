import os
import sys
from datetime import datetime


def create_file() -> None:
    """Create directories and files with numbered content."""
    args = sys.argv[1:]

    directories = []
    filename = None

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    if "-d" in args:
        d_index = args.index("-d")
        directories = [
            arg for arg in args[d_index + 1:]
            if arg != "-f" and arg != filename
        ]

    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if filename is None:
        return

    filepath = os.path.join(directory_path, filename)

    lines = []

    while True:
        content = input("Enter content line: ")

        if content == "stop":
            break

        lines.append(content)

    if not lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a+", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)
        is_new_file = file.tell() == 0

        if is_new_file:
            file.write(timestamp + "\n")
        else:
            file.write("\n\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


create_file()
