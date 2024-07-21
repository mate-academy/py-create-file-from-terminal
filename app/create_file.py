import sys
import os
from datetime import datetime


def create_directories(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str) -> None:
    # Append timestamp and content to file
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.strip().lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            directories = args[d_index + 1:]
            file_name = None
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        directories = None
    else:
        print("Usage: python create_file.py -d dir1 dir2 -f file.txt")
        print("or: python create_file.py -f file.txt")

    if directories:
        path = create_directories(directories)
    else:
        path = os.getcwd()

    # Create file if specified
    if file_name:
        file_path = os.path.join(path, file_name)
        write_to_file(file_path)
    elif directories:
        print(f"Created directories: {os.path.join(*directories)}")


if __name__ == "__main__":
    main()
