import sys
import os
from datetime import datetime


def create_directories(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_or_append_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File {file_path} exists, appending content.")
    else:
        print(f"Creating new file: {file_path}")

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. Use -d for directories and -f for file.")
        return

    dir_path = []
    file_name = None
    index = 0

    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and args[index] != "-f":
                dir_path.append(args[index])
                index += 1
        elif args[index] == "-f":
            index += 1
            if index < len(args):
                file_name = args[index]
                index += 1
        else:
            index += 1

    if dir_path:
        create_directories(dir_path)

    if file_name:
        if dir_path:
            file_path = os.path.join(*dir_path, file_name)
        else:
            file_path = file_name
        create_or_append_file(file_path)


if __name__ == "__main__":
    main()
