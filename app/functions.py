import sys
from datetime import datetime


def validator(command: list) -> object:
    if (
        len(command) >= 4
        and command[0] == "-d"
        and "-f" in command[2:]
        and command[-1] != "-f"
    ):
        # print("Third case")
        return 3
    elif command[0] == "-d" and len(command) >= 2:
        # print("First case")
        return 1
    elif command[0] == "-f" and len(command) == 2:
        # print("Second case")
        return 2


def fill_the_file() -> str:
    line_data_number, data = 1, ""

    for line in sys.stdin:
        if line.rstrip() == "stop":
            break
        data += f"{line_data_number} {line}"
        line_data_number += 1
    return f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n" + data


def dir_and_file_name_extraction(command: list) -> dict:
    dirs_file_info = {"dirs": [], "file_name": command[-1]}

    for elem in command[1:]:
        if elem != "-f":
            dirs_file_info["dirs"].append(elem)
        else:
            break
    return dirs_file_info
