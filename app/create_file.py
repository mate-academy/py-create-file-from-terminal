import os
import sys
from datetime import datetime


def create_directory(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

    return path


def create_file(file_path: str) -> None:
    is_file_existing = os.path.isfile(file_path)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if is_file_existing:
            file.write("\n")

        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line{line_number}: ")

            if content.lower() == "stop":
                break

            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print(
            "Usage format: python create_file.py "
            "[-d dir1 dir2...] [-f file.txt]"
        )

    directories = []
    file_name = ""

    index = 0
    while index < len(args):
        if args[index] == "-d":
            index += 1

            while index < len(args) and args[index] != "-f":
                directories.append(args[index])
                index += 1

        if index < len(args) and args[index] == "-f":
            index += 1
            file_name = args[index]

        index += 1

    if not directories and not file_name:
        print("You must specify at least -d or -f option.")

        return

    if directories:
        directory_path = create_directory(directories)
    else:
        directory_path = os.getcwd()

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)
        print(f"Created {file_name} file at: {directory_path}")
    else:
        print(f"Created directory at: {directory_path}")


if __name__ == "__main__":
    main()
