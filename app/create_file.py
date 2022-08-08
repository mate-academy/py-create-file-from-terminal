import os
import sys
from datetime import datetime


def input_info(file_name: str):
    date = datetime.now()
    date.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{date}\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            print(line, file=file)


def get_command():
    command_arguments = sys.argv

    if "-d" in command_arguments and \
            "-f" in command_arguments:
        _, d_flag, *directories, f_flag, file_name = command_arguments
        path = "/".join(directories)
        os.makedirs(path, exist_ok=True)
        input_info(path + "/" + file_name)

    elif "-d" in command_arguments:
        _, _, *directories = command_arguments
        path = "/".join(directories)
        os.makedirs(path, exist_ok=True)

    elif "-f" in command_arguments:
        _, _, file_name = command_arguments
        input_info(file_name)


get_command()
