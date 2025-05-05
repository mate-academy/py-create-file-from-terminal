import os
import sys
from datetime import datetime


dir_path = ""
file_path = ""


def make_directory() -> None:
    global dir_path

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_parts = []

        for i in range(d_index + 1, len(sys.argv)):
            if sys.argv[i].startswith("-"):
                break
            dir_parts.append(sys.argv[i])

        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)


def make_file() -> None:
    global file_path

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        with open(file_path, "a"):
            pass


def add_content_to_file() -> None:
    if not file_path:
        print("Error: file path not set, you fucking idiot! Use -f to specify a file.")
        return

    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")
        f.write("\n")
