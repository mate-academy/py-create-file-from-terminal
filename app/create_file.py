
import os
import sys
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

            if (
                index < len(arguments)
                and arguments[index] not in ("-d", "-f")
            ):
                filename = arguments[index]
                index += 1

        else:
            print("Invalid argument")
            return

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = "."

    if filename is None:
        return

    file_path = os.path.join(directory_path, filename)
    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(content_lines, start=1):
            file.write(f"{number} {line}\n")


create_file()
