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
    print(command[command.index("-f")])
    create_file(command[command.index("-f") + 1])

if "-d" in command and "-f" not in command:
    dirs = command[command.index("-d") + 1:]
    path = dirs[0]
    for direct in dirs[1:]:
        path += f"/{direct}"
    create_dir(path)
if "-f" in command and "-d" in command:
    dirs = command[command.index("-d") + 1: command.index("-f")]
    path = dirs[0]
    for direct in dirs[1:]:
        path += f"/{direct}"
    create_dir(path)
    file_name = command[command.index("-f") + 1]
    path += f"/{file_name}"
    create_file(path)
