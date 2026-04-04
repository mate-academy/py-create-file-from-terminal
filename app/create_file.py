import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        line_number = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:

    file_index = -1
    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")

    dir_index = -1
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d")

    if file_index != -1:
        file_name = sys.argv[file_index + 1]
        if dir_index != -1:
            if dir_index < file_index:
                directory_path = (
                    os.path.join(*sys.argv[dir_index + 1:file_index]))
            else:
                directory_path = os.path.join(*sys.argv[dir_index + 1:])
            os.makedirs(directory_path, exist_ok=True)
            file_path = os.path.join(directory_path, file_name)

        else:
            file_path = file_name

        create_file(file_path)

    if dir_index != -1 and "-f" not in sys.argv:
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        os.makedirs(directory_path, exist_ok=True)


if __name__ == "__main__":
    main()
