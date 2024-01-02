import os
import sys
from datetime import datetime


def create_directory(*directories: str) -> str:
    path = os.path.join(os.getcwd(), *directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(name_file: str, path: str) -> None:
    name_file = os.path.join(path, name_file) if path else name_file
    with open(name_file, "a") as file:
        if file.tell() > 0:
            file.write("\n\n")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_date}")
        line_number = 1
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"\n{line_number} {content}")
            line_number += 1


def parsing_values_from_terminal(input_data: list) -> None:
    path = None
    flag_index_d = input_data.index("-d") if "-d" in input_data else None
    flag_index_f = input_data.index("-f") if "-f" in input_data else None
    if flag_index_d:
        directory_args = input_data[flag_index_d + 1: flag_index_f]
        path = create_directory(*directory_args)
    if flag_index_f:
        create_file(input_data[flag_index_f + 1], path)


if __name__ == "__main__":
    parsing_values_from_terminal(sys.argv)
