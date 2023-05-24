import os
import sys
from datetime import datetime


def create_directory(console_data: list[str]) -> None:
    parent_dir: str = console_data[console_data.index("-d") + 1]

    dir_indices = [i for i, arg in enumerate(console_data) if arg == "-d"]
    dir_names = [console_data[i + 1] for i in dir_indices]

    for dir_name in dir_names:
        path: str = os.path.join(parent_dir, dir_name)
        os.makedirs(path, exist_ok=True)


def create_file(console_data: list[str]) -> None:
    if "-d" in console_data:
        parent_dir: str = console_data[console_data.index("-d") + 1]
        new_dir: str = console_data[console_data.index("-d") + 2]
        file_name: str = console_data[console_data.index("-f") + 1]
        file_path: str = os.path.join(parent_dir, new_dir, file_name)
    else:
        file_path: str = console_data[console_data.index("-f") + 1]

    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        counter: int = 0

        while True:
            message: str = input("Enter content line: ")
            counter += 1
            if message == "stop":
                break
            file.write(f"{counter} {message}\n")
        file.write("\n")


if __name__ == "__main__":
    console_data: list[str] = sys.argv

    if "-d" in console_data:
        create_directory(console_data)

    if "-f" in console_data:
        create_file(console_data)
