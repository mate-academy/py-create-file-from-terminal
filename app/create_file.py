import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def write_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_num = 0
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            line_num += 1
            file.write(f"{line_num} {content}\n")


def work_with_commands() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        dir_path = os.path.join(*args[dir_index + 1:file_index])
        create_directory(dir_path)
        file_name = args[file_index + 1]
        file_path = os.path.join(dir_path, file_name)
        write_content(file_path)
    elif "-d" in args:
        dir_index = args.index("-d")
        dir_path = os.path.join(*args[dir_index + 1:])
        create_directory(dir_path)
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        write_content(file_name)


if __name__ == "__main__":
    work_with_commands()
