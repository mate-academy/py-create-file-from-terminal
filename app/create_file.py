from datetime import datetime
import os
import sys
from os.path import exists


def create_directories(start: int, end: int) -> str:
    directories_list = sys.argv[start: end]
    path_directories = "/".join(directories_list)
    os.makedirs(path_directories)
    return path_directories


def create_file(file_name: str) -> None:
    if exists(file_name):
        write_content_from_terminal(file_name, "a")
    elif exists(file_name) is False:
        write_content_from_terminal(file_name, "w")


def write_content_from_terminal(path_to_file: str, method: str) -> None:
    content_from_terminal = input("Enter content line: ")
    with open(f"{path_to_file}", f"{method}") as new_file:
        print(new_file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"))
        file_line_number = 1
        while content_from_terminal != "stop":
            new_file.write(f"{file_line_number} {content_from_terminal}\n")
            content_from_terminal = input("Enter content line: ")
            file_line_number += 1
            if content_from_terminal == "stop":
                break


if "-d" in sys.argv and "-f" in sys.argv:
    range_start = sys.argv.index("-d") + 1
    range_end = len(sys.argv) - range_start
    path_directory = create_directories(range_start, range_end)
    path_file = os.path.join(path_directory, sys.argv[-1])
    write_content_from_terminal(path_file, "w")

elif "-f" in sys.argv:
    create_file(sys.argv[-1])

elif "-d" in sys.argv:
    range_start = sys.argv.index("-d") + 1
    range_end = len(sys.argv)
    create_directories(range_start, range_end)
