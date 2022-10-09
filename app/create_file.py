import os
import sys
from datetime import datetime


def file_write(file_name: str) -> None:

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            line = input("Enter content line>>>")
            if line == "stop":
                file.write("\n")
                break
            file.write(line + "\n")


def dir_create(command: list[str]) -> str:
    path = ""

    for folder in command[command.index("-d") + 1:]:
        if folder == "-f":
            break
        path = os.path.join(path, folder)

    if not os.path.isdir(path):
        os.makedirs(path)

    return path


command = sys.argv

while "exit" not in command:
    path = ""

    if "-d" in command:
        path = dir_create(command)

    if "-f" in command:
        file_name = os.path.join(path, command[command.index("-f") + 1])
        file_write(file_name)

    command = input("Press exit or enter command>>>")
    command = command.split()
