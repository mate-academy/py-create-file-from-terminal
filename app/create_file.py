import sys
import os
from datetime import datetime


def create_directories(path_components: list[str]) -> str:
    path = os.path.join(*path_components)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

    return path


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"\n{timestamp}\n")
        line_number = 1

        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1

    print(f"File updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)

    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if not file_name:
        if directories:
            print(
                "Directories created successfully. No file specified."
                " Use the -f flag to create or update a file."
            )
        else:
            print(
                "Error: No file specified. "
                "Use the -f flag to create or update a file."
            )
        sys.exit(1)

    target_path = os.getcwd()
    if directories:
        target_path = create_directories(directories)

    if file_name:
        file_path = os.path.join(target_path, file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    main()
