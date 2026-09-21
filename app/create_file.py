import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dirs = []
    file_name = None

    _ = 0
    while _ < len(args):
        if args[_] == "-d":
            _ += 1
            while _ < len(args) and not args[_].startswith("-"):
                dirs.append(args[_])
                _ += 1
        elif args[_] == "-f":
            _ += 1
            if _ < len(args):
                file_name = args[_]
                _ += 1
        else:
            _ += 1

    dir_path = ""
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        filepath = os.path.join(dir_path, file_name) if dir_path else file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_is_not_empty = (os.path.exists(filepath)
                             and os.path.getsize(filepath) > 0)

        with open(filepath, "a") as f:
            if file_is_not_empty:
                f.write("\n")

            f.write(f"{timestamp}\n")
            for index, line_content in enumerate(lines, 1):
                f.write(f"{index} {line_content}\n")


create_file()
