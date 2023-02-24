import os
from sys import argv
from datetime import datetime


def create_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []
    line_number = 1

    if os.path.exists(file_path):
        with open(file_path) as f:
            content = f.readlines()
        line_number = len(content) + 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(f"{line_number} {line}\n")
        line_number += 1

    with open(file_path, "w") as f:
        f.write(f"{timestamp}\n")
        f.writelines(content)


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def main() -> None:
    if "-d" in argv:
        dir_flag_index = argv.index("-d")
        dir_path = os.path.join(*argv[dir_flag_index + 1:])
        create_directory(dir_path)
    elif "-f" in argv:
        file_flag_index = argv.index("-f")
        file_name = argv[file_flag_index + 1]
        file_path = os.path.abspath(file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
