import os
import datetime
import sys


def make_dirs(abs_path: str, dirs_to_create: list[str]) -> None:
    new_path = abs_path
    for directory in dirs_to_create:
        os.mkdir(os.path.join(new_path, directory))
        os.chdir(os.path.join(new_path, directory))
        new_path = os.getcwd()


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

    if "-d" in terminal_input:
        if "-f" not in terminal_input:
            make_dirs(
                home_path,
                terminal_input[terminal_input.index("-d") + 1:]
            )
        else:
            make_dirs(
                home_path,
                terminal_input[
                    terminal_input.index("-d") + 1: terminal_input.index("-f")
                ]
            )
            new_file_with_content(
                terminal_input[terminal_input.index("-f") + 1]
            )
    else:
        new_file_with_content(terminal_input[terminal_input.index("-f") + 1])
