import os
import sys
from datetime import datetime


def file_write(file_name: str, path: str = "") -> None:
    with open(path + file_name, "a") as file:
        line = ""
        file.write(datetime.now().strftime("%y-%m-%d %H:%M:%S\n"))
        while line != "stop":
            line = input("Enter content line>>>")
            file.write(line)


def dir_create(command: list[str]) -> str:
    path = ""
    for folder in command:
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
        file_name = command[command.index("-f") + 1]
        file_write(file_name, path)

    command = input("Press exit or enter command>>>")
    command = command.split()
