import os
import sys
from datetime import datetime


def create_file(directory: list, filename: str) -> None:
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
    if filename:
        filepath = os.path.join(*directory, filename)
        with open(filepath, "a") as file_handle:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_handle.write(timestamp + "\n")
            line_number = 1
            while True:
                line = input("Enter content line:")
                if line == "stop":
                    break
                file_handle.write(f"{line_number} {line}\n")
                line_number += 1


def main() -> None:
    args = sys.argv[1:]
    directory = []
    filename = ""

    if "-d" in args:
        flag_index = args.index("-d")
        directory = args[flag_index + 1:]

    if "-f" in args:
        flag_index = args.index("-f")
        filename = args[flag_index + 1]

    create_file(directory, filename)


if __name__ == "__main__":
    main()
