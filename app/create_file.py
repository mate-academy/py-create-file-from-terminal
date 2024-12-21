import sys
import os
from datetime import datetime
from typing import List


def main() -> None:
    args: List[str] = sys.argv[1:]
    if not args:
        print("No arguments provided. Use -d for directories or -f for files.")
        return

    if "-d" in args:
        process_directories(args)

    if "-f" in args:
        process_file(args)

    else:
        print("No valid options provided. Please provide -d for directories "
              "or -f for files.")


def process_directories(args: List[str]) -> None:
    """
    Create directories based on -d flag
    """
    dir_index = args.index("-d") + 1
    dirs: List[str] = []
    while dir_index < len(args) and args[dir_index] != "-f":
        dirs.append(args[dir_index])
        dir_index += 1

    if dirs:
        try:
            path = os.path.join(*dirs)
            os.makedirs(path, exist_ok=True)
            print(f"Directory created: {path}")
        except PermissionError:
            print(f"Permission denied to create directory: {path}")
        except Exception as e:
            print(f"Failed to create directory {path}: {e}")
    else:
        print("No directories specified after -d.")


def process_file(args: List[str]) -> None:
    """
    Create or overwrite files based on -f flag
    """
    file_index = args.index("-f") + 1
    if file_index >= len(args):
        print("No file specified after -f.")
        return

    filename = args[file_index]
    content_lines: List[str] = []
    print("Enter content line (type 'stop' to finish):")

    while True:
        line: str = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines: List[str] = [
        f"{timestamp}\n"
    ] + [f"{i + 1} {line}" for i, line in enumerate(content_lines)]

    file_path = os.path.join(".", filename)
    with open(file_path, "a") as file:
        file.writelines(formatted_lines)

    print(f"File '{file_path}' created/updated.")


if __name__ == "__main__":
    main()
