import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_or_append_file(file_path: str) -> None:
    """Create or append to file, adding timestamp
    and user content with line numbers."""
    with open(file_path, "a") as file:
        # Write timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1

    print(f"File written: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    # Check for -d and -f flags
    if "-d" not in args and "-f" not in args:
        print("Error: You must provide either -d or -f flag.")
        return

    directory_path = []
    file_name = None

    # Parse arguments for -d and -f flags
    if "-d" in args:
        dir_index = args.index("-d")
        for arg in args[dir_index + 1:]:
            if arg == "-f":
                break
            directory_path.append(arg)

    if "-f" in args:
        file_index = args.index("-f")
        if len(args) > file_index + 1:
            file_name = args[file_index + 1]
        else:
            print("Error: File name is missing after -f flag.")
            return

    # Construct the full path
    if directory_path:
        dir_path = os.path.join(*directory_path)
        create_directory(dir_path)
    else:
        dir_path = ""

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        create_or_append_file(file_path)
    elif dir_path:
        # Only create directories if only -d flag is present
        print("Directory structure created successfully.")
    else:
        print("Error: Invalid arguments.")


if __name__ == "__main__":
    main()
