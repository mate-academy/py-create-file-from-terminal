import os
import sys

from datetime import datetime
from typing import Union


def get_directory_path(args: list) -> Union[str | None]:
    if "-d" not in args:
        return None

    start_index = args.index("-d") + 1
    end_index = len(args)

    if "-f" in args:
        index_f = args.index("-f")
        end_index = index_f if index_f > start_index else len(args)

    return (
        str(os.path.join(*args[start_index:end_index]))
        if end_index != -1
        else str(os.path.join(*args[start_index:]))
    )


def get_file_name(args: list) -> Union[str, None]:
    if "-f" not in args:
        return None

    args_str = "".join(args)

    start_index = args_str.index("-f") + 2
    index_d = args_str.find("-d")
    end_index = index_d if index_d > start_index else len(args_str)

    return (
        args_str[start_index:end_index]
        if end_index != -1
        else args_str[start_index:]
    )


def create_file(file_path: Union[str, None]) -> None:
    with open(file_path, "a") as file:
        if file.tell() != 0:
            file.write("\n\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_number = 1
        while (content_line := input("Enter content line: ")) != "stop":
            file.write(f"\n{line_number} {content_line}")
            line_number += 1


def create_file_from_terminal() -> None:
    arguments = sys.argv
    directory_path = get_directory_path(arguments)
    file_name = get_file_name(arguments)

    if directory_path and file_name:
        os.makedirs(directory_path, exist_ok=True)
        create_file(os.path.join(directory_path, file_name))
    elif directory_path:
        os.makedirs(directory_path)
    elif file_name:
        create_file(file_name)


if __name__ == "__main__":
    create_file_from_terminal()
