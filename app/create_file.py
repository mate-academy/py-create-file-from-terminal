import sys
import os
from datetime import datetime


def create_path(directories_list: list) -> str:
    path = os.path.join(*directories_list)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(file_path, "a") as file:
            file.write(f"{current_time}\n")

        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                with open(file_path, "a") as file:
                    file.write("\n")
                break
            with open(file_path, "a") as file:
                file.write(f"{line} {content}\n")
            line += 1
    else:
        print(f"File '{file_path}' already exists.")


def terminal() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        command_d, *directories = args
        create_path(directories)

    elif "-f" in args:
        create_file(args[-1])


if __name__ == "__main__":
    terminal()