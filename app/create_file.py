import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file_with_content(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_num = 0
    with open(file_path, "a" if os.path.exists(file_path) else "w") as file:
        file.write(timestamp)
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            line_num += 1
            file.write(f"Line{line_num} {content}\n")


def work_with_commands() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")

        dir_path = os.path.join(*args[dir_index + 1:file_index])
        file_name = args[file_index + 1]

        create_directory(dir_path)
        file_path = os.path.join(dir_path, file_name)
        create_file_with_content(file_path)
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        create_file_with_content(file_name)
    elif "-d" in args:
        dir_index = args.index("-d")
        dir_path = os.path.join(*args[dir_index + 1:])
        create_directory(dir_path)


if __name__ == "__main__":
    work_with_commands()
