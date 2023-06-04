import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv
    if "-d" in args and "-f" not in args:
        dir_index = args.index("-d")
        directory_path = os.path.join(*args[dir_index + 1:])
        create_directory(directory_path)
    if "-f" and "-d" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        dir_index = args.index("-d")
        directory_path = os.path.join(*args[dir_index + 1:file_index])
        create_directory(directory_path)
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)
    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        create_file(file_name)


def create_directory(path: str) -> None:
    os.makedirs(path)
    print(f"Directory created: {path}")


def create_file(file_name: str) -> None:
    mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, mode) as file:
        file.write(datetime.now().strftime("&Y-%m-%d, %H:%M:%S\n"))
        num = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(str(num) + " " + content + "\n")
            num += 1
