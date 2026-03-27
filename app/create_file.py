import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    d_idx = args.index("-d") if "-d" in args else None
    f_idx = args.index("-f") if "-f" in args else None

    if d_idx is not None:
        if f_idx is not None and f_idx > d_idx:
            parts = args[d_idx + 1: f_idx]
        else:
            parts = args[d_idx + 1:]
        dir_path = os.path.join(*parts)

    if f_idx is not None:
        file_name = args[f_idx + 1]

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        full_path = os.path.join(dir_path, file_name)

        with open(full_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + "\n")

            for i, line in enumerate(content_lines, start=1):
                file.write(f"{i} {line}\n")

            file.write("\n")
