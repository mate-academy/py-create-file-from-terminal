import os
import sys
from datetime import datetime

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_flag_values(arguments: list, flag: str) -> list:
    if flag not in arguments:
        return []
    start_index = arguments.index(flag) + 1
    end_index = len(arguments)
    for other_flag in ("-d", "-f"):
        if other_flag in arguments[start_index:]:
            end_index = arguments.index(other_flag, start_index)
    return arguments[start_index:end_index]


def write_content(file_path: str) -> None:
    is_existing_file = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a") as output_file:
        if is_existing_file:
            output_file.write("\n")
        current_time = datetime.now().strftime(TIMESTAMP_FORMAT)
        output_file.write(f"{current_time}\n")

        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break
            output_file.write(f"{line_number} {content_line}\n")
            line_number += 1


directories = get_flag_values(sys.argv, "-d")
file_names = get_flag_values(sys.argv, "-f")

if directories:
    os.makedirs(os.path.join(*directories), exist_ok=True)

if file_names:
    write_content(os.path.join(*directories, file_names[0]))
