import sys
import os
from datetime import datetime


def create_directory_file():

    directory_parts = []
    filename = None

    i = 1
    while i < len(sys.argv):

        if sys.argv[i] == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                directory_parts.append(sys.argv[i])
                i += 1
            continue

        if sys.argv[i] == "-f":
            if i + 1 < len(sys.argv):
                filename = sys.argv[i + 1]
                i += 2
                continue
            else:
                print("Provide filename after -f")
                return

        i += 1

    if directory_parts:
        directory = os.path.join(*directory_parts)
        os.makedirs(directory, exist_ok=True)

    else:
        directory = os.getcwd()

    if filename is None:
        print("Provide filename after -f")
        return

    file_path = os.path.join(directory, filename)

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            lines.append(line)

        except (KeyboardInterrupt, EOFError):
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{timestamp}\n")
        for ind, line in enumerate(lines, 1):
            f.write(f"{ind} {line}\n")
        f.write("\n")
