import os
import sys
from datetime import datetime


def validator(command: list) -> object:
    if "-d" in command and "-f" in command:
        return 3
    elif command[0] == "-d" and len(command) >= 2:
        return 1
    elif command[0] == "-f" and len(command) == 2:
        return 2


def processed_input_data() -> str:
    line_data_number, data = 1, ""

    for line in sys.stdin:
        if line.rstrip() == "stop":
            break
        data += f"{line_data_number} {line}"
        line_data_number += 1
    return f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n" + data


def existing_file_content(file_path: str) -> str:
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            file_content = f.read()
    else:
        file_content = ""
    return file_content


def content_to_file(file_content: str, file_name: str) -> None:
    starting_indent = "" if len(file_content) == 0 else "\n"
    with open(file_name, "a") as f:
        info_to_write = (
            starting_indent + processed_input_data().rstrip("\n")
        )
        f.write(info_to_write)


def dir_and_file_name_extraction(command: list) -> dict:
    dirs_file_info = {"dirs": [], "file_name": ""}

    f_cmd_index = command.index("-f")
    d_cmd_index = command.index("-d")

    dirs_file_info["file_name"] = command[f_cmd_index + 1]
    if f_cmd_index < d_cmd_index:
        dirs_file_info["dirs"] = command[d_cmd_index + 1 :]
    elif d_cmd_index < f_cmd_index:
        dirs_file_info["dirs"] = command[
            d_cmd_index + 1 : f_cmd_index
        ]

    return dirs_file_info
