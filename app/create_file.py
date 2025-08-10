import os
import sys
from datetime import datetime


def write_file(file_path: str) -> None:
    with open(f"{file_path}", "a") as new_file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(time + "\n")
        while True:
            row = input("Enter content line: ")
            if row == "stop":
                break
            new_file.write(row + "\n")


def create_path(full_path: list) -> str:
    index_path = full_path.index("-d") + 1
    parts_of_path = []
    while index_path < len(full_path) and full_path[index_path] != "-f":
        parts_of_path.append(full_path[index_path])
        index_path += 1
    path = os.path.join(*parts_of_path)
    return path


def create_file() -> None:
    full_path = sys.argv
    file_name = ""
    path = ""
    if "-f" in full_path:
        index_file_name = full_path.index("-f") + 1
        file_name = full_path[index_file_name]
    if "-d" in full_path:
        path = create_path(full_path)
    if path:
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, file_name)
    else:
        file_path = file_name
    write_file(file_path)


if __name__ == "__main__":
    create_file()
