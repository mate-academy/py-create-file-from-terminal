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


if sys.argv[1] == "-d" and len(sys.argv) == 6 and sys.argv[4] == "-f":
    path_directories = os.path.join(sys.argv[2], sys.argv[3])
    os.makedirs(path_directories)
    path_file = os.path.join(sys.argv[2], sys.argv[3], sys.argv[5])
    write_content_from_terminal(path_file, "w")


if sys.argv[1] == "-d" and len(sys.argv) == 5 and sys.argv[3] == "-f":
    path_directory = sys.argv[2]
    os.makedirs(path_directory)
    path_file = os.path.join(sys.argv[2], sys.argv[4])
    write_content_from_terminal(path_file, "w")


if sys.argv[1] == "-f" and exists(f"{sys.argv[2]}") is True:
    path_file = sys.argv[2]
    write_content_from_terminal(path_file, "a")

if sys.argv[1] == "-f" and exists(f"{sys.argv[2]}") is False:
    path_file = sys.argv[2]
    write_content_from_terminal(path_file, "w")


if sys.argv[1] == "-d" and len(sys.argv) == 3:
    os.makedirs(sys.argv[2])

if sys.argv[1] == "-d" and len(sys.argv) == 4:
    path_directories = os.path.join(sys.argv[2], sys.argv[3])
    os.makedirs(path_directories)
