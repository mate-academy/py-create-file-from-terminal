import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    filepath = os.path.join(directory, filename)
    mode = "a" if os.path.exists(filepath) else "w"

    with open(filepath, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        line_number = 1
        while True:
            content_line = input(f"Enter content line {line_number}: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = os.path.join(*sys.argv[dir_index:file_index])
        filename = sys.argv[file_index]
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        filename = input("Enter file name: ")
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        directory = os.getcwd()
        filename = sys.argv[file_index]
    create_file(directory, filename)


if __name__ == "__main__":
    main()
