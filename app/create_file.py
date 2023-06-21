import sys
import os
from datetime import datetime


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(file_name: str) -> None:
    enter = ""
    data = ""
    index = 1
    while enter != "stop":
        enter = input("Enter content line: ")
        if enter != "stop":
            data += f"{index} {enter} \n"
            index += 1
    with open(file_name, "a") as file:
        now = datetime.now()
        file.writelines(now.strftime("%Y-%m-%d %H:%M:%S"))
        file.writelines("\n")
        file.writelines(data)
        file.writelines("\n")


command = sys.argv
if "-f" in command and "-d" not in command:
    create_file(command[command.index("-f") + 1])

if "-d" in command and "-f" not in command:
    dirs = command[command.index("-d") + 1:]
    path = os.path.join(*dirs)
    create_dir(path)

if "-f" in command and "-d" in command:
    dirs = command[command.index("-d") + 1: command.index("-f")]
    path = os.path.join(*dirs)
    create_dir(path)
    file_name = command[command.index("-f") + 1]
    path = os.path.join(path, file_name)
    create_file(path)
