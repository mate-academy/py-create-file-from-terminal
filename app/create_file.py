import os
import sys
from datetime import datetime
from typing import List


def create_file(directory: List[str], filename: str) -> None:
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        if filename:
            filename = os.path.join(directory_path, filename)

    if filename:
        with open(filename, "a") as file_handle:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_handle.write(timestamp + "\n")

            print("Enter content line:")
            line_number = 1
            while True:
                line = input("Enter content line:")
                if line == "stop":
                    break
                file_handle.write(f"{line_number} {line}\n")
                line_number += 1


def parse_arguments() -> tuple:
    args = sys.argv[1:]
    if "-d" in args:
        flag_index = args.index("-d")
        directory = args[flag_index + 1:args.index("-f")] \
            if "-f" in args else args[flag_index + 1:]
    else:
        directory = []

    if "-f" in args:
        flag_index = args.index("-f")
        filename = args[flag_index + 1]
    else:
        filename = ""

    return directory, filename


def main() -> None:
    directory, filename = parse_arguments()
    create_file(directory, filename)


if __name__ == "__main__":
    main()
