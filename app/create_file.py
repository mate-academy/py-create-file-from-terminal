import sys
import os
from datetime import datetime


def create_dir(directories: list) -> None:
    path = os.path.join(os.getcwd(), *directories)
    try:
        os.makedirs(path)
        os.chdir(path)
    except FileExistsError:
        os.chdir(path)


def clean_directory(terminal_directory: list, that_we_delete: list) -> list:
    terminal_directory.remove("app/create_file.py")
    for index in that_we_delete:
        terminal_directory.remove(index)
    return terminal_directory


def create_file(file_name: str) -> None:
    line_number = 1
    type_line = f"Line{line_number}"
    if os.path.exists(file_name):
        type_line = "Another"
    with open(file_name, "a") as terminal_file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        terminal_file.write(date_time + "\n")
        while True:
            content = input("Enter content line:")
            if content != "stop":
                terminal_file.write(f"{type_line} {content} \n")
                line_number += 1
                continue
            break


terminal_list = sys.argv
if "-d" in terminal_list and "-f" in terminal_list:
    file_name = terminal_list[-1]
    directory = clean_directory(terminal_list, ["-d", "-f", file_name])
    create_dir(directory)
    create_file(file_name)

elif "-d" in terminal_list and "-f" not in terminal_list:
    directory = clean_directory(terminal_list, ["-d"])
    create_dir(directory)
    create_file("file.txt")

elif "-d" not in terminal_list and "-f" in terminal_list:
    directory = clean_directory(terminal_list, ["-f"])
    create_file(directory[-1])
