import sys
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)
    # print(f"Directory '{directory_path}' created or already exists.")


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    print("Enter")

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} Line{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d <directory_path> -f <file_name>")

    dir_path = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    directory = os.path.join(dir_path) if dir_path else ""

    if directory:
        create_directory(directory)

    if file_name:
        file_path = os.path.join(directory, file_name)
        write_to_file(file_path)
    else:
        print("No file name provided.")


if __name__ == "__main__":
    main()
