import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_or_append_file(path: str, filename: str) -> None:
    full_path = os.path.join(path, filename) if path else filename
    file_exists = os.path.isfile(full_path)

    content_lines: list[str] = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_path, "a" if file_exists else "w", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")
        f.write(timestamp + "\n")

        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args or ("-d" not in args and "-f" not in args):
        print("Use the following template: "
              "python create_file.py -d dir_path -f filename")
        return

    directory_path = ""
    filename = ""
    read_dir = False
    read_file = False

    for arg in args:
        if arg == "-d":
            read_dir = True
            read_file = False
            continue
        elif arg == "-f":
            read_file = True
            read_dir = False
            continue

        if read_dir:
            directory_path = (
                os.path.join(directory_path, arg)
                if directory_path else arg
            )
        elif read_file:
            filename = arg
            break

    if directory_path:
        create_directory(directory_path)

    if filename:
        create_or_append_file(directory_path, filename)


if __name__ == "__main__":
    main()
