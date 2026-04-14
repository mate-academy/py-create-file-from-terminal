import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv
    directory_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            path_parts.append(arg)
        directory_path = os.path.join(*path_parts) if path_parts else ""

        if directory_path:
            os.makedirs(directory_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: -f flag requires a filename.")
            return

    if not file_name:
        return

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    full_path = os.path.join(directory_path, file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(content_lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


if __name__ == "__main__":
    create_file()
