import os
import sys
from datetime import datetime


def work_with_folder(command_list: list[str]) -> None:
    global destination
    destination = os.path.join(command[command.index("-d") + 1])
    os.makedirs(destination, exist_ok=True)


def work_with_file(command_list: list[str]) -> None:
    file_name = command[command.index("-f") + 1]
    new_file_path = os.path.join(destination, file_name)
    with open(new_file_path, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        text = input("Enter content line: ")
        while text != "stop":
            new_file.write(text + "\n")
            text = input("Enter content line: ")
        new_file.write("\n")


if __name__ == '__main__':
    command = sys.argv

    try:
        work_with_folder(command)
    except ValueError:
        destination = ""
    try:
        work_with_file(command)
    except ValueError:
        pass

