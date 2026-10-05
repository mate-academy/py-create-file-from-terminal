import os
import sys
from datetime import datetime


def create_file_from_terminal() -> None:
    directories = []
    filename = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                directories.append(sys.argv[i])
                i += 1
        elif sys.argv[i] == "-f":
            i += 1
            if i < len(sys.argv):
                filename = sys.argv[i]
                i += 1
        else:
            i += 1

    dir_path = os.path.join(*directories) if directories else "."
    if directories:
        os.makedirs(dir_path, exist_ok=True)

    if filename is None:
        return

    file_path = os.path.join(dir_path, filename)
    separator = ""

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "rb") as existing_file:
            existing_file.seek(-1, os.SEEK_END)
            ends_with_newline = existing_file.read(1) == b"\n"
        separator = "\n" if ends_with_newline else "\n\n"

    with open(file_path, "a", encoding="utf-8") as output_file:
        output_file.write(separator)
        output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break

            output_file.write(f"{line_number} {content}\n")
            line_number += 1


if __name__ in ("__main__", "<run_path>"):
    create_file_from_terminal()
