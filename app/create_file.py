import os
import sys
from datetime import datetime
from typing import Optional


def create_directories(directory_path: str) -> None:
    """
    Creates a directory or nested directories.

    Args:
        directory_path (str): The path to the directory to be created.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully.")
    except Exception as e:
        print(f"Failed to create directory '{directory_path}': {e}")


def write_to_file(file_path: str) -> None:
    """
    Writes content to a file. Adds a timestamp and prepends line numbers.

    Args:
        file_path (str): The path of the file to write content to.
    """
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            print(f"File {file_path} already exists. Appending new content...")
        else:
            print(f"Creating new file: {file_path}")

        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")
            line_number = 1

            while True:
                content_line = input(f"Enter content line ({line_number}): ")
                if content_line.lower() == "stop":
                    break
                file.write(f"{line_number} {content_line}\n")
                line_number += 1

        print(f"Content successfully written to '{file_path}'.")

    except Exception as e:
        print(f"Failed to write to file {file_path}: {e}")


def main() -> None:
    """
    Main function to handle arguments and execute appropriate operations.
    """
    args = sys.argv[1:]

    if not args or ("-d" not in args and "-f" not in args):
        print("Usage:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        return

    directory: Optional[str] = None
    file_name: Optional[str] = None
    if "-d" in args:
        d_index = args.index("-d") + 1
        directory = os.path.join(*args[d_index:])

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    if directory:
        create_directories(directory)

    if file_name:
        file_path = os.path.join(directory or "", file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    main()
