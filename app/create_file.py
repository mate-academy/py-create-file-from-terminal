import os
import sys
from datetime import datetime


def create_directory(directories: list[str]) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_name: str) -> None:
    file_content = []
    line = ""
    write_method = "w"
    line_number = 1

    while line != "stop":
        line = input("Enter content line: ")
        file_content.append(f"{line_number} " + line + "\n")
        line_number += 1

    file_content = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
    ] + file_content
    if os.path.exists(file_name):
        write_method = "a"
        file_content = ["\n"] + file_content

    with open(file_name, write_method) as file:
        for line in file_content[:-1]:
            file.write(line)


if "-d" in sys.argv and "-f" in sys.argv:
    index_of_f = sys.argv.index("-f")
    path = create_directory(sys.argv[2:index_of_f])
    path = os.path.join(path, sys.argv[index_of_f + 1])
    create_file(path + sys.argv[index_of_f + 1])

if "-f" in sys.argv and "-d" not in sys.argv:
    create_file(sys.argv[2])

if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory(sys.argv[2:])
