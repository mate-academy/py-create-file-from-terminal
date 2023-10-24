import os
import sys
from typing import List, Tuple
import datetime


def run_create_file(directory_path: list,
                    file_name: str | None,
                    file_content: list | None) -> None:

    parent_dir = os.getcwd()

    if directory_path and file_name and file_content:
        create_directories_and_file_name(directory_path=directory_path,
                                         parent_dir=parent_dir,
                                         file_content=file_content)

    if directory_path and file_name is None:
        create_directories(directory_path=directory_path,
                           parent_dir=parent_dir)

    if file_name is not None and not directory_path:
        create_file_name(parent_dir=parent_dir,
                         file_content=file_content)


def create_file_name(parent_dir: str, file_content: list) -> None:

    file_path = os.path.join(parent_dir, file_name)
    with open(file_path, "a") as file:
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(date_now + "\n")
        for content_idx, content in enumerate(file_content):
            file.write(f"{content_idx + 1} {content}")
        file.write("\n")


def create_directories(directory_path: list, parent_dir: str) -> None:
    path = os.path.join(parent_dir, *directory_path)
    os.makedirs(path, exist_ok=True)


def create_directories_and_file_name(directory_path: list,
                                     parent_dir: str,
                                     file_content: list) -> None:

    path = os.path.join(parent_dir, *directory_path)
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, file_name)

    with open(file_path, "a") as file:
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(date_now + "\n")
        for content_idx, content in enumerate(file_content):
            file.write(f"{content_idx + 1} {content}")
        file.write("\n")


def divide_user_terminal_input_into_dir_and_filename(
        user_terminal_input: list) -> Tuple[List[str], str]:

    directories = []
    file_name = None

    for _ in user_terminal_input:
        if "-d" in user_terminal_input and "-f" in user_terminal_input:
            d_index = user_terminal_input.index("-d")
            f_index = user_terminal_input.index("-f")

            directories = user_terminal_input[d_index + 1:f_index]
            file_name = user_terminal_input[f_index + 1]

        if "-d" in user_terminal_input and "-f" not in user_terminal_input:
            d_index = user_terminal_input.index("-d")
            directories = user_terminal_input[d_index + 1:]

        if "-f" in user_terminal_input and "-d" not in user_terminal_input:
            f_index = user_terminal_input.index("-f")
            file_name = user_terminal_input[f_index + 1]

    return directories, file_name


def get_user_input() -> list:

    users_input_content = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        users_input_content.append(user_input + "\n")

    return users_input_content


if __name__ == "__main__":

    directories, file_name = divide_user_terminal_input_into_dir_and_filename(
        user_terminal_input=sys.argv)

    if file_name:
        file_content = get_user_input()
    else:
        file_content = []

    run_create_file(directory_path=directories,
                    file_name=file_name,
                    file_content=file_content)
