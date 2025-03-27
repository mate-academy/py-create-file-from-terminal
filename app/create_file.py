import sys
import os
from datetime import datetime


def create_directory(path_parts: any) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: any) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dir] -f [file]")
        return

    dir_path, file_name = [], None

    while args:
        arg = args.pop(0)
        if arg == "-d":
            while args and args[0] != "-f":
                dir_path.append(args.pop(0))
        elif arg == "-f" and args:
            file_name = args.pop(0)

    if not file_name:
        print("File name is required.")
        return

    full_dir = create_directory(dir_path) if dir_path else os.getcwd()
    file_path = os.path.join(full_dir, file_name)
    write_to_file(file_path)


if __name__ == "__main__":
    main()
