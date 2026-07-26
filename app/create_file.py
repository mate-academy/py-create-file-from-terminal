import sys
import os
from datetime import datetime


def create_file(path_of_file):
    with open(path_of_file, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            data = input("Enter information: ")
            if data == "stop":
                break
            file.write(f"{data}\n")


def get_command(command_string: list):
    if "-d" in command_string and "-f" not in command_string:
        args = command_string[2:]
        path_dir = os.path.join(*args)
        os.makedirs(path_dir)
    if "-d" in command_string and "-f" in command_string:
        args = command_string[2:-2]
        path_dir = os.path.join(*args)
        os.makedirs(path_dir)
        path_file = path_dir + "/" + command_string[-1]
        create_file(path_file)
    if "-d" not in command_string and "-f" in command_string:
        path_file = command_string[-1]
        create_file(path_file)


if __name__ == '__main__':
    get_command(sys.argv)
