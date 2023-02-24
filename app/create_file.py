import datetime
import os
import sys


args = sys.argv[1:]


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path: str = None) -> None:
    if path is not None:
        file_name = f"{path}\\{args[-1]}"
    else:
        file_name = f"{args[-1]}"
    with open(file_name, "a") as file:
        lines = [f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                lines.append("\n")
                break
            lines.append(f"{new_line}\n")
        file.writelines(lines)


if "-d" in args and "-f" not in args:
    path = os.path.join(*args[1:])
    create_directory(path)

elif "-d" not in args and "-f" in args:
    create_file()

elif "-d" in args and "-f" in args:
    path = os.path.join(*args[:-2])
    create_directory(path)
    create_file(path)
