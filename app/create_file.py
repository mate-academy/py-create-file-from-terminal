from datetime import datetime
import os

import sys


def create_directories(folders: list) -> None:
    for i in range(len(folders)):
        os.mkdir(folders[i])
        os.chdir(folders[i])
        print(os.getcwd())


def work_with_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        time = datetime.now().strftime("%y-%m-%d %H:%M:%S") + "\n"
        file.write(time)

        line = input("Enter content line:")

        while line != "stop":
            file.write(line + "\n")
            line = input("Enter content line:")
        file.write("\n")


def controller() -> None:

    command_list = sys.argv

    if "-d" in command_list and "-f" not in command_list:
        folder_list = command_list[2:]
        create_directories(folder_list)
        print("Folders were added")

    if "-f" in command_list and "-d" not in command_list:
        work_with_file(command_list[2])
        print("File was created")

    if "-d" in command_list and "-f" in command_list:
        create_directories(command_list[2: -2])
        print("Folders were added")
        work_with_file(command_list[-1])
        print("File was created")


if __name__ == "__main__":
    controller()
