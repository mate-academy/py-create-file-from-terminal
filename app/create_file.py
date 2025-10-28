import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    directories = []
    file_name = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
        elif arg == "-f":
            mode = "file"
        else:
            if mode == "dir":
                directories.append(arg)
            elif mode == "file" and file_name is None:
                file_name = arg

    folder_path = None
    if directories:
        folder_path = os.path.join(*directories)
        os.makedirs(folder_path, exist_ok=True)

    if file_name:
        if folder_path:
            full_path = os.path.join(folder_path, file_name)
        else:
            full_path = file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(full_path, "a") as output_file:
            output_file.write(timestamp + "\n")
            for line_number, content in enumerate(lines, start=1):
                output_file.write(f"{line_number} {content}\n")
            output_file.write("\n")
