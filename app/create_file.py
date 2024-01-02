import os
import sys
from datetime import datetime


def create_directory(directory1: str, directory2: str) -> str:
    path = os.path.join(os.getcwd(), directory1, directory2)
    os.makedirs(path)
    return path


def create_file(name_file: str, path: str) -> None:
    name_file = os.path.join(path, name_file) if path else name_file
    with open(name_file, "a") as file:
        if file.tell() != 0:
            file.write("\n")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_date}\n")
        line_number = 1
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def parsing_values_from_terminal(terminal_input: list) -> None:
    path = None
    if "-d" in terminal_input:
        index_d = terminal_input.index("-d")
        directory_args = terminal_input[index_d + 1: index_d + 3]
        path = create_directory(*directory_args)
    if "-f" in terminal_input:
        name_file = terminal_input[terminal_input.index("-f") + 1]
        create_file(name_file, path)


if __name__ == "__main__":
    parsing_values_from_terminal(sys.argv)
