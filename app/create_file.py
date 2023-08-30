import os
import sys
from datetime import datetime


def create_file(
    directory: str,
    filename: str
) -> None:
    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n")
    else:
        with open(file_path, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        with open(file_path, "a") as file:
            file.write(f"{line_number} {line}\n")
        line_number += 1


def create_directory(directory: str) -> None:
    os.makedirs(directory)


def main() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        directories = sys.argv[d_index + 1:]
        for directory in directories:
            create_directory(directory)
    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        filename = sys.argv[f_index + 1]
        create_file(".", filename)


if __name__ == "__main__":
    main()
