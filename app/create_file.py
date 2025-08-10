import argparse
import os
from datetime import datetime


def parse_command_line_args() -> tuple:
    parser = argparse.ArgumentParser("create_file_from_terminal")
    parser.add_argument("-d", nargs="*", default=[""])
    parser.add_argument("-f", default="")

    dirs_path: list[str] = parser.parse_args().d
    file_path: str = parser.parse_args().f

    return os.path.join(*dirs_path), file_path


def get_date_writing() -> str:
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S\n")


def get_data_from_input() -> list[str]:
    count_content = 1
    user_content = []

    while True:
        input_content = input("Enter content line: ")

        if input_content.lower() == "stop":
            break

        user_content.append(f"{count_content} {input_content}\n")
        count_content += 1

    return user_content


def write_data(
    file_path: str,
    user_data: list[str],
) -> None:
    with open(file_path, "a") as source_file:
        if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
            source_file.write("\n")

        source_file.write(get_date_writing())
        source_file.writelines(user_data)


def run() -> None:
    dirs_path, file_path = parse_command_line_args()

    if len(dirs_path):
        os.makedirs(dirs_path, exist_ok=True)

    if len(file_path):
        abs_path = os.path.join(dirs_path, file_path)
        write_data(abs_path, get_data_from_input())
