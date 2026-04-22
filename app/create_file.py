import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i].startswith("-"):
                break
            directories.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    current_path = ""
    if directories:
        current_path = os.path.join(*directories)
        os.makedirs(current_path, exist_ok=True)

    if file_name:
        full_path = os.path.join(current_path, file_name)
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        is_file = os.path.exists(full_path)
        should_add_blank_line = is_file and os.path.getsize(full_path) > 0

        with open(full_path, "a") as f:
            if should_add_blank_line:
                f.write("\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")

            for i, content in enumerate(lines, 1):
                f.write(f"{i} {content}\n")


create_file()
