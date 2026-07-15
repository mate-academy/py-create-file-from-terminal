import sys
import os
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str]:

    is_d_present = "-d" in arguments
    is_f_present = "-f" in arguments

    if is_d_present:
        index_d = arguments.index("-d")

    if is_f_present:
        index_f = arguments.index("-f")

    parsed_directories = []

    if is_d_present:
        for item in arguments[index_d + 1:]:
            if item == "-f":
                break
            parsed_directories.append(item)

    parsed_file_name = ""

    if is_f_present:
        parsed_file_name = arguments[index_f + 1]

    return parsed_directories, parsed_file_name


def create_directories(directory_list: list[str]) -> str:
    created_path = ""
    if directory_list:
        created_path = os.path.join(*directory_list)
        os.makedirs(created_path, exist_ok=True)
    return created_path


def get_formatted_time() -> str:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def write_content_to_file(target_file_name: str, target_path: str) -> None:
    if target_file_name:
        full_path = os.path.join(target_path, target_file_name)
        file_exists = os.path.exists(full_path)

        line_number = 1
        with open(full_path, "a") as file:

            if file_exists:
                file.write("\n")
            file.write(get_formatted_time() + "\n")

            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1


directories, file_name = parse_arguments(sys.argv)
path = create_directories(directories)
write_content_to_file(file_name, path)
