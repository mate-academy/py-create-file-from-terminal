import os
import argparse
from datetime import datetime


def create_directory(directory_path: str) -> None:
    """Create the directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)


def append_lines_to_file(path: str) -> None:
    """
    Append lines to the file with line numbers, starting from the
    last line number.
    """
    with open(path, "a+") as file:
        file.seek(0)
        lines = file.readlines()
        start_line = 0

        if lines:
            file.write("\n")

        file.seek(0, os.SEEK_END)
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
            directory_path, args.file
        )
        append_lines_to_file(file_path)


if __name__ == "__main__":
    main()
