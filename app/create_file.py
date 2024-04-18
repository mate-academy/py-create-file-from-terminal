import os
import argparse
from datetime import datetime


def create_directory(directory_path: str) -> None:
    """Create the directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)


def get_last_line_number(path: str) -> int:
    """
    Return the number of lines in a file, or 0 if the file does not exist.
    """
    try:
        with open(path, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0


def append_lines_to_file(path: str, start_line: int) -> None:
    """
    Append lines to the file with line numbers, starting from the
    last line number.
    """
    with open(path, "a" if start_line > 0 else "w") as file:
        if not start_line:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            content = input("Enter content ('stop' to finish): ")

            if content == "stop":
                break

            start_line += 1
            file.write(f"{start_line} {content}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a file in specified directory."
    )
    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        required=False,
        help="Path to the directory: `-d dir1 dir2`.",
    )
    parser.add_argument(
        "-f", "--file", required=False, help="Specify the filename to create."
    )
    args = parser.parse_args()
    directory_path = os.path.join(
        ".", *args.directory if args.directory else ""
    )

    if args.directory:
        create_directory(directory_path)

    if args.file:
        file_path = os.path.join(
            directory_path if args.directory else ".", args.file
        )
        last_line = get_last_line_number(file_path)
        append_lines_to_file(file_path, last_line)


if __name__ == "__main__":
    main()
