import os
import sys
from datetime import datetime


def create_file_with_content(file_path: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")
    line_count = 1
    while True:
        content_line = input("Enter content line: ")
        if content_line.lower() == "stop":
            break
        with open(file_path, "a") as file:
            file.write(f"{line_count} {content_line}\n")
        line_count += 1
    with open(file_path, "a") as file:
        file.write("\n")


def main() -> None:
    directory_path = ""

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        directory_path = os.path.join(*sys.argv[dir_index + 1: f_index])
        os.makedirs(directory_path, exist_ok=True)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]

        if "-d" in sys.argv:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        create_file_with_content(file_path)


if __name__ == "__main__":
    main()
