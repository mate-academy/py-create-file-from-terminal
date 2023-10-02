import sys
import os
from datetime import datetime


def make_directory(path_to_file: list) -> str:
    path = os.path.join(*path_to_file)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(directory_path: str, file_name: str) -> None:
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n")

    show_time = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    with open(file_path, "w") as file:
        file.write(show_time)

    row = 1
    while True:
        content = input("Enter content: ")
        if content == "stop":
            break
        file.write(f"{row} {content}\n")
        row += 1


def main() -> None:
    terminal_info = sys.argv
    if "-f" in terminal_info and "-d" in terminal_info:
        start_index = terminal_info.index("-d") + 1
        end_index = terminal_info.index("-f")
        path = make_directory(terminal_info[start_index:end_index])
        name_of_file = terminal_info[terminal_info.index("-f") + 1]
        create_file(name_of_file, path)
    if "-f" in terminal_info:
        create_file(terminal_info[terminal_info.index("-f") + 1])
    elif "-d" in terminal_info:
        make_directory(terminal_info[terminal_info.index("-d") + 1:])


if __name__ == "__main__":
    main()
