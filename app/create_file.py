import sys
import os
from datetime import datetime


def create_file_with_content(file_path: str) -> None:
    """
    Creates a file with user-inputted content and timestamps the content.
    If the file already exists, appends new content below the existing one.
    """
    # Check if the file exists
    file_exists = os.path.exists(file_path)

    # Open the file in append mode
    with open(file_path, "a") as file:
        if not file_exists:
            print(f"Creating new file: {file_path}")
        else:
            print(f"Appending to existing file: {file_path}")

        # Add a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        # Accept content from the user
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    """
    Parses command-line arguments and performs actions -d and -f.
    """
    # Parse arguments
    args = sys.argv[1:]

    if not args or "-h" in args or "--help" in args:
        print(
            "Usage:\n"
            "  python create_file.py -d <dir1> <dir2> ... -f <filename>\n"
            "  python create_file.py -d <dir1> <dir2> ...\n"
            "  python create_file.py -f <filename>\n"
        )
        return

    # Flags
    dir_path = []
    file_name = None

    # Parse -d and -f flags
    if "-d" in args:
        d_index = args.index("-d")
        # Collect directory arguments
        dir_path = args[d_index + 1:]
        if "-f" in dir_path:
            f_index = dir_path.index("-f")
            file_name = dir_path[f_index + 1]
            dir_path = dir_path[:f_index]

    if "-f" in args and not file_name:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    # If only -d was provided
    if dir_path and not file_name:
        full_dir_path = os.path.join(*dir_path)
        os.makedirs(full_dir_path, exist_ok=True)
        print(f"Directory created: {full_dir_path}")

    # If -f was provided
    elif file_name:
        if dir_path:
            # Create directories if -d was also provided
            full_dir_path = os.path.join(*dir_path)
            os.makedirs(full_dir_path, exist_ok=True)
            print(f"Directory created: {full_dir_path}")
            file_path = os.path.join(full_dir_path, file_name)
        else:
            file_path = file_name

        # Create or append content to the file
        create_file_with_content(file_path)

    else:
        print("Invalid arguments. Use -h or --help for usage instructions.")


if __name__ == "__main__":
    main()
