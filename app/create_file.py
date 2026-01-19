import sys
import os
from datetime import datetime


def create_directory(path_components: list[str]) -> None:
    path = os.path.join(*path_components)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        mode = "a"
        print(f"Appending content to existing file '{file_path}'.")
    else:
        mode = "w"
        print(f"Creating new file '{file_path}'.")

    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line ({line_number}): ")
            if content.strip().lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2] [-f filename]")
        return

    if "-d" in args:
        dir_index = args.index("-d")
        dir_components: list[str] = []

        if "-f" in args:
            file_index = args.index("-f")
            dir_components = args[dir_index + 1:file_index]
            file_name = args[file_index + 1] if (
                len(args) > file_index + 1
            ) else None
        else:
            dir_components = args[dir_index + 1:]
            file_name = None

        if not dir_components:
            print("Error: No directories specified after -d flag.")
            return

        create_directory(dir_components)

        if file_name:
            file_path = os.path.join(*dir_components, file_name)
            create_file(file_path)
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1] if (
            len(args) > file_index + 1
        ) else None

        if not file_name:
            print("Error: No file name specified after -f flag.")
            return

        create_file(file_name)
    else:
        print("Usage: python create_file.py [-d dir1 dir2] [-f filename]")


if __name__ == "__main__":
    main()
