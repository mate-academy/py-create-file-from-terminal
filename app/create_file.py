import os
import sys
from datetime import datetime


def create_directory(path: list) -> None:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        if os.path.exists(file_path):
            file.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        line_number = 1

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    flag = sys.argv[1]

    if flag == "-d" and "-f" not in sys.argv:
        create_directory(sys.argv[2:])

    elif flag == "-f" and "-d" not in sys.argv:
        create_file(sys.argv[2])

    elif flag == "-d" and "-f" in sys.argv:
        f_index = sys.argv.index("-f")

        directory_parts = sys.argv[2:f_index]
        create_directory(directory_parts)

        file_name = sys.argv[f_index + 1]
        file_path = os.path.join(*directory_parts, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
