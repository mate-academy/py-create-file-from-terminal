import os
import sys
from datetime import datetime


destination = ""


def work_with_folder(command_list: list[str]) -> None:
    global destination
    destination = os.path.join(command_list[command_list.index("-d") + 1])
    os.makedirs(destination, exist_ok=True)


def work_with_file(command_list: list[str]) -> None:
    file_name = command_list[command_list.index("-f") + 1]
    new_file_path = os.path.join(destination, file_name)
    with open(new_file_path, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        text = input("Enter content line: ")
        while text != "stop":
            new_file.write(text + "\n")
            text = input("Enter content line: ")
        new_file.write("\n")


def terminal_command(command: list[str]) -> None:
    try:
        work_with_folder(command)
    except ValueError:
        pass
    try:
        work_with_file(command)
    except ValueError:
        pass


if __name__ == "__main__":
    terminal_command(sys.argv)
