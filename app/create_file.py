import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path)
    os.chdir(os.getcwd() + "/" + path)


def create_file(file_name: str) -> None:
    count = 1
    file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content += "\n" + str(count) + " " + line
        count += 1
    with open(file_name, "w") as file:
        file.write(file_content)


command = sys.argv

if "-d" in command and "-f" not in command:
    path = "/".join(command[2:])
    create_directory(path)
if "-d" not in command and "-f" in command:
    file_name = command[2]
    create_file(file_name)
if "-d" in command and "-f" in command:
    index_f_flag = command.index("-f")
    file_name = command[index_f_flag + 1]
    path = "/".join(command[2:index_f_flag])
    create_directory(path)
    create_file(file_name)
