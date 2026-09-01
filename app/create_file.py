import os
import sys
from datetime import datetime
from typing import TextIO


def write_content(file_object: TextIO, file_exists: bool) -> None:
    """Write timestamp and user-entered content to the file."""
    if file_exists:
        file_object.write("\n")

    now = datetime.now()
    file_object.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")

    line_counter = 1

    while True:
        temp_str = input("Enter content line: ")

        if temp_str == "stop":
            break

        file_object.write(f"{line_counter} {temp_str}\n")
        line_counter += 1


def make_dirs(directories: list[str]) -> str:
    """Create directories and return their path."""
    directory_path = os.path.join(*directories)

    os.makedirs(directory_path, exist_ok=True)

    return directory_path


command_list = sys.argv

d_index = (
    command_list.index("-d")
    if "-d" in command_list
    else None
)

f_index = (
    command_list.index("-f")
    if "-f" in command_list
    else None
)

if d_index is not None and f_index is not None:
    if d_index > f_index:
        directories = command_list[d_index + 1:]
    else:
        directories = command_list[d_index + 1:f_index]

    file_name = command_list[f_index + 1]
    directory_path = make_dirs(directories)
    file_path = os.path.join(directory_path, file_name)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file_object:
        write_content(file_object, file_exists)

elif d_index is not None:
    directories = command_list[d_index + 1:]
    make_dirs(directories)

elif f_index is not None:
    file_name = command_list[f_index + 1]
    file_exists = os.path.exists(file_name)

    with open(file_name, "a") as file_object:
        write_content(file_object, file_exists)
