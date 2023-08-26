import os
import sys
from datetime import datetime


def validator(command: list) -> object:
    if "-d" in command and "-f" in command:
        # print("Third case")
        return 3
    elif command[0] == "-d" and len(command) >= 2:
        # print("First case")
        return 1
    elif command[0] == "-f" and len(command) == 2:
        # print("Second case")
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
    if len(file_content) == 0:
        with open(file_name, "a") as f:
            info_to_write = processed_input_data().rstrip("\n")
            f.write(info_to_write)
    else:
        with open(file_name, "a") as f:
            info_to_write = "\n" * 2 + processed_input_data().rstrip(
                "\n"
            )
            f.write(info_to_write)


def dir_and_file_name_extraction(command: list) -> dict:
    dirs_file_info = {"dirs": [], "file_name": ""}

    index_of_flag = command.index("-f")
    dirs_file_info["dirs"] = command[1:index_of_flag]
    dirs_file_info["file_name"] = command[index_of_flag + 1]

    return dirs_file_info
