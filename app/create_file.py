import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    directories = []
    filename = None

    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1

            while i < len(args) and args[i] not in ("-d", "-f"):
                directories.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1

            if i < len(args):
                filename = args[i]
                i += 1

        else:
            i += 1

    if directories:
        directory = os.path.join(*directories)
        os.makedirs(directory, exist_ok=True)
    else:
        directory = "."

    if filename is None:
        return

    filepath = os.path.join(directory, filename)

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file:
        if os.path.getsize(filepath) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


create_file()
