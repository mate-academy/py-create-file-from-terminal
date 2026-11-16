from sys import argv
import os
from datetime import datetime

command_entered = argv

result_dict = {}

flag = ""
for command in command_entered:
    if command.startswith("-"):
        flag = command
        if flag not in result_dict:
            result_dict[flag] = []
        continue
    if flag:
        result_dict[flag].append(command)


def create_dir() -> str:
    path = ""
    for directory in result_dict.get("-d", ""):
        path = os.path.join(path, directory)
    if not path:
        return ""
    os.makedirs(path, exist_ok=True)
    return path


def create_file() -> None:
    file_name = result_dict["-f"][0]
    line_nr = 0
    path = create_dir()
    if path:
        file_name = os.path.join(path, file_name)

    with open(file_name, "a") as file:
        if open(file_name, "r").read():
            file.write("\n")

        file.write(datetime.strftime(datetime.now(),
                                     "%Y-%m-%d %H:%M:%S\n"))
        while True:
            line_nr += 1
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_nr} {user_input}\n")


if result_dict.get("-f"):
    create_file()
if result_dict.get("-d", None):
    create_dir()
