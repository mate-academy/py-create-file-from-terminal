import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"{file_path} already exists. Appending content.")
        with open(file_path, "r") as f:
            lines = f.readlines()
        last_number = max([int(line.split()[0])
                           for line in lines[1:] if line.strip()
                           and line.split()[0].isdigit()],
                          default=0)
    else:
        print(f"{file_path} does not exist. Creating new file.")
        last_number = 0

    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                break
            last_number += 1
            f.write(f"{last_number} {line_content}\n")

    print(f"Content written to {file_path}.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py "
              "-d for <directory> -f for <filename>")
        sys.exit(1)

    directory = None
    file_name = None
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            dir_parts = []
            while i < len(args) and args[i] != "-f":
                dir_parts.append(args[i])
                i += 1
            directory = os.path.join(*dir_parts)
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
            i += 1
        else:
            i += 1

    if directory:
        create_directory(directory)
        if file_name:
            file_path = os.path.join(directory, file_name)
            create_file(file_path)
        else:
            print(f"Directory '{directory}' created. No file specified.")
    elif file_name:
        create_file(file_name)
    else:
        print("Invalid arguments. "
              "Please use '-d' for directory or '-f' for file.")
