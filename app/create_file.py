import sys
import os
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created at: {path}")
    return path


def write_content_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []

    # Capture input lines until "stop"
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1

    # Append new content with timestamp
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")  # Add spacing if the file already has content
        file.write(f"{timestamp}\n")
        file.write("\n".join(content_lines))

    print(f"Content added to {file_path}")


def main() -> None:
    args = sys.argv[1:]
    if "-f" not in args and "-d" not in args:
        print("Please specify either -d (directory) or -f (file) flag.")
        return

    if "-d" in args:
        # Handle directory creation
        dir_index = args.index("-d") + 1
        path_parts = args[dir_index:]
        dir_path = create_directory(path_parts)
    else:
        dir_path = os.getcwd()  # Use current directory if no directory flag

    if "-f" in args:
        # Handle file creation
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(dir_path, file_name)

        # Create file if it does not exist
        open(file_path, "w").close()  # Creates file if it doesn't exist
        print(f"File created at: {file_path}")

        # Write content to file
        write_content_to_file(file_path)


if __name__ == "__main__":
    main()
