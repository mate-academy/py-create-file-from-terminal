import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> str | bytes:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def create_or_append_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        f.seek(0)
        content = f.read().strip()
        f.write("\n\n" if content else "")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        line_number = 1 if not content else content.count("\n\n") + 1
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1

    print(f"File written: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
            path = create_directory(dir_parts)
            file_path = os.path.join(path, file_name)
            create_or_append_file(file_path)
        else:
            dir_parts = args[d_index + 1:]
            create_directory(dir_parts)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = os.path.join(os.getcwd(), file_name)
        create_or_append_file(file_path)
