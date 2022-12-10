from datetime import datetime
import os
import sys
from os.path import exists


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
    directories_list = []
    for i in range(2, len(sys.argv) - 2):
        directories_list.append(sys.argv[i])
    path_directory = "/".join(directories_list)
    os.makedirs(path_directory)
    path_file = os.path.join(path_directory, sys.argv[-1])
    write_content_from_terminal(path_file, "w")

elif "-d" in sys.argv and "-f" not in sys.argv:
    directories_list = []
    for i in range(2, len(sys.argv)):
        directories_list.append(sys.argv[i])
    path_directory = "/".join(directories_list)
    os.makedirs(path_directory)

elif "-f" in sys.argv and "-d" not in sys.argv:
    if exists(f"{sys.argv[-1]}"):
        write_content_from_terminal(sys.argv[-1], "a")
    elif exists(f"{sys.argv[-1]}") is False:
        write_content_from_terminal(sys.argv[-1], "w")
