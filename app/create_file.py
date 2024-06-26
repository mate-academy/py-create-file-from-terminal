import argparse
import os
from typing import List


def create_file(file_name: str, directories: List[str]) -> None:
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as f:
            f.write("")  # Write an empty file
        print(f"Created file: {file_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a file in specified directories.")
    parser.add_argument("-f", "--file", required=True,
                        help="Name of the file to create.")
    parser.add_argument("-d", "--directories", nargs="+", required=True,
                        help="Directories where the file should be created.")
    args = parser.parse_args()

    create_file(args.file, args.directories)


if __name__ == "__main__":
    main()
