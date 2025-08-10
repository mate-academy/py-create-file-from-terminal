import os
import sys
from datetime import datetime


def create_dict(dirs: list) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path)
    return path


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Enter content lines (type 'stop' to finish):")

    content_lines = []
    while True:
        line = input("Enter line: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
            file.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py "
              "-d [directory parts] -f [file name]")
        return

    args = sys.argv[1:]
    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for item in args[d_index + 1:]:
            if item == "-f":
                break
            directory_parts.append(item)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    target_path = os.getcwd()
    if directory_parts:
        target_path = create_dict(directory_parts)
        print(f"Directory created: {target_path}")

    if file_name:
        file_path = os.path.join(target_path, file_name)
        write_to_file(file_path)
        print(f"File created/updated at: {file_path}")
