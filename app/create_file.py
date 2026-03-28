import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv

    i = 1
    dirs = []
    file_name = None

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1

        elif args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
            i += 2

        else:
            i += 1

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    if not file_name:
        return

    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")
        file.write("\n")


if __name__ == "__main__":
    create_file()
