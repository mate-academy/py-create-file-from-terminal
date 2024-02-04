import os.path
from datetime import datetime
from sys import argv

command = argv
command_list = command.split()


def management_by_terminal() -> None:
    if "-d" in command and "-f" not in command:
        create_dir()
    elif "-f" in command and "-d" not in command:
        create_file()
    elif "-f" in command and "-d" in command:
        create_dir()
        create_file()


def create_file() -> None:
    if "-f" in command_list:
        index = command_list.index("-f")
        file_name = command_list[index + 1]
        path_file = os.path.join(*file_name.split("/"))
        time_now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(path_file, "a") as file:
            file.write(f"\n\n{time_now_str}")


def create_dir() -> None:
    if "-d" in command_list:
        index = command_list.index("-d")
        path_dirs = command_list[index + 1:]
        path_dir = os.path.join(*path_dirs)
        os.makedirs(path_dir, exist_ok=True)
