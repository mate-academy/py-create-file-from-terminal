import sys
import os

from datetime import datetime


def create_path(dirs):
    directories_to_add = "/".join(dirs)

    if not os.path.exists(directories_to_add):
        os.makedirs(directories_to_add)

    return directories_to_add


def create_file(path: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a") as file:
        counter = 1
        file.write(f"{now}\n")
        while True:
            message = input("Enter content line: ")
            if message == "stop":
                break
            file.writelines(f"{counter} {message}\n")
            counter += 1


input_data = sys.argv

if "-d" in input_data and "-f" not in input_data:
    directories = input_data[2:]
    create_path(directories)


if "-f" in input_data and "-d" not in input_data:
    file_name = input_data[2]
    create_file(file_name)

if "-d" in input_data and "-f" in input_data:
    filename = input_data[-1]
    directories = input_data[2:-2]
    create_file(create_path(directories) + filename)
