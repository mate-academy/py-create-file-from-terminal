import datetime
import os.path
import sys


def create_directory(path_parts: str) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    append_mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, append_mode) as file:
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2] [-f filename]")
        sys.exit(1)

    directory = []
    file_name = None

    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directory = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            directory = args[d_index + 1:]

    if "-f" in args and not file_name:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if directory:
        path = create_directory(directory)
    else:
        path = os.getcwd()

    if file_name:
        file_path = os.path.join(path, file_name)
        create_file(file_path)
