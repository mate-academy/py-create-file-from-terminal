import os
import sys
from datetime import datetime


def create_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        print("input content lines until you input 'stop'")

        lines_count = 0

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            lines_count += 1
            file.write(str(lines_count) + " " + line + "\n")


input_list = sys.argv

if "-d" in input_list and "-f" not in input_list:
    path = os.path.join(*input_list[input_list.index("-d") + 1:])
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Path already exists")

if "-f" in input_list and "-d" not in input_list:
    create_file(input_list[input_list.index("-f") + 1])

if "-f" in input_list and "-d" in input_list:

    path = os.path.join(
        *input_list[input_list.index("-d") + 1: input_list.index("-f")]
    )
    if not os.path.exists(path):
        os.makedirs(path)

    create_file(input_list[input_list.index("-f") + 1], path)
