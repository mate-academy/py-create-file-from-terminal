import sys
import os
from datetime import datetime


def create_file() -> None:
    arguments = sys.argv[1:]

    directories = []
    filename = None

    index = 0

    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1

            while (
                index < len(arguments)
                and arguments[index] not in ("-d", "-f")
            ):
                directories.append(arguments[index])
                index += 1

        elif arguments[index] == "-f":
            index += 1

            if index < len(arguments):
                filename = arguments[index]
                index += 1
            else:
                raise ValueError("File name is missing")

        else:
            raise ValueError("Unknown argument")

    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if filename is None:
        return

    file_path = os.path.join(directory_path, filename)

    content_lines = []
    line_number = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(f"{line_number} {line}")
        line_number += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for line in content_lines:
            file.write(f"{line}\n")


create_file()
