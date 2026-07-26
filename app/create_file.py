import os
import sys
from datetime import datetime


path = ""


def create_file_content(path_to_file: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    list_of_content = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        list_of_content.append(content)

    with open(path_to_file, "a") as file:
        file.write(f"\n{timestamp}\n")
        file.write("\n".join(list_of_content) + "\n")


if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        path_list = sys.argv[d_index + 1: f_index]
        filename = sys.argv[f_index + 1]
    else:
        path_list = sys.argv[d_index + 1:]

    path = os.path.join(*path_list)
    if not os.path.exists(path):
        os.makedirs(path)

if "-f" in sys.argv:
    path_to_file = os.path.join(path, sys.argv[-1])
    create_file_content(path_to_file)
