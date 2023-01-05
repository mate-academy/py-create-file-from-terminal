import os
import datetime
import sys


def make_dirs(abs_path: str, dirs_to_create: list[str]) -> None:
    for directory in dirs_to_create:
        abs_path = os.path.join(abs_path, directory)

    os.makedirs(abs_path)
    os.chdir(abs_path)


def new_file_with_content(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        current_time = datetime.datetime.now()
        str_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(str_current_time + "\n")

        while True:
            line_number = 0
            content = input("Enter content line: ")

            if content == "stop":
                break
            line_number += 1
            new_file.write(f"{line_number} {content}\n")


def create_file() -> None:
    home_path = os.getcwd()
    terminal_input = sys.argv
    f_index = terminal_input.index("-f") if "-f" in terminal_input else False
    d_index = terminal_input.index("-d") if "-d" in terminal_input else False

    if d_index:
        if f_index:
            make_dirs(
                home_path,
                terminal_input[d_index + 1: f_index]
            )
            new_file_with_content(terminal_input[f_index + 1])
        else:
            make_dirs(
                home_path,
                terminal_input[d_index + 1:]
            )
    else:
        new_file_with_content(terminal_input[f_index + 1])
