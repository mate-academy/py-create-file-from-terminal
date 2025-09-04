import os
import datetime
import sys
from typing import Optional


list_of_args = sys.argv[1:]


def create_file_with_content(list_of_args: list) -> Optional[str]:
    if "-d" in list_of_args and "-f" in list_of_args:
        d_index = list_of_args.index("-d")
        f_index = list_of_args.index("-f")
        dirs_path = list_of_args[d_index + 1:f_index]
        file_name = list_of_args[f_index + 1]
        os.makedirs(os.path.join(*dirs_path), exist_ok=True)
        full_path = os.path.join(*dirs_path, file_name)
        return full_path

    elif "-d" in list_of_args:
        d_index = list_of_args.index("-d")
        if d_index + 1 >= len(list_of_args):
            raise ValueError("Directory names are missing after -d flag")
        dirs_path = list_of_args[d_index + 1:]
        full_path_for_d = os.path.join(*dirs_path)
        os.makedirs(full_path_for_d, exist_ok=True)
        return None

    elif "-f" in list_of_args:
        f_index = list_of_args.index("-f")
        if f_index + 1 >= len(list_of_args):
            raise ValueError("File name is missing after -f flag")
        file_name = list_of_args[f_index + 1]
        parent_dir = os.path.dirname(file_name)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        return file_name

    else:
        raise ValueError(
            "No valid flags provided. Use -d for directories and/or -f for file name."
        )


def get_file_content() -> list:
    content_of_file = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_of_file.append(line)
    return content_of_file


def write_to_file(file_path: str, content_of_file: list) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_newline = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as file:
        if add_newline:
            file.write("\n")  # только между блоками
        file.write(f"{timestamp}\n")

        for index, line in enumerate(content_of_file, start=1):
            file.write(
                f"{index} {line}\n"
            )


if __name__ == "__main__":
    file_path = create_file_with_content(list_of_args)
    if file_path:  # записываем только если есть файл
        lines = get_file_content()
        write_to_file(file_path, lines)
