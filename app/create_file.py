import os
import sys
from datetime import datetime


def create_directory(path_parts: list) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []

    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as f:
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"File created/updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = args[d_index + 1:]
        if "-f" in dir_path:
            f_index = dir_path.index("-f")
            dir_path = dir_path[:f_index]
        if dir_path:
            create_directory(dir_path)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        if "-d" in args:
            d_index = args.index("-d")
            dir_path = args[d_index + 1:f_index]
            file_path = os.path.join(*dir_path, file_name)
        else:
            file_path = file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
