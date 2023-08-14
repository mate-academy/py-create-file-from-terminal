import os
import argparse
from datetime import datetime as dt


def time_stamp() -> str:
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="+",
        help="List of directories to create files in"
    )
    parser.add_argument("-f", help="Name of the file to create")
    args = parser.parse_args()
    return args


def create_new_file(directory_list: list = None, filename: str = None) -> None:
    if directory_list:
        dir_and_file_name = os.path.join(*directory_list, filename)
    else:
        dir_and_file_name = os.path.join(os.getcwd(), filename)

    with open(dir_and_file_name, "a") as file:
        string_counter = 1
        file.write(f"{time_stamp()}\n")

        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{string_counter} {content}\n")
            string_counter += 1
        file.write("\n")


def create_path(directory_list: list) -> None:
    parent_dir = os.getcwd()
    path_with_new_dirs = os.path.join(parent_dir, *directory_list)
    os.makedirs(path_with_new_dirs, exist_ok=True)
