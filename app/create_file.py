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


path = ""
if result_dict.get("-d", None):
    for directory in result_dict["-d"] :
        path = os.path.join(path, directory)
    os.makedirs(path, exist_ok=True)


if result_dict.get("-f", None):
    file_name = result_dict["-f"][0]
    user_input = ""
    i = 0
    if path:
        file_name = os.path.join(path, file_name)

    with open(file_name, "a") as f:
        if open(file_name, "r").read():
            f.write("\n")

        f.write(datetime.strftime(datetime.now(),
                                  "%Y-%m-%d %H:%M:%S\n"))
        while True:
            i += 1
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{i} {user_input}\n")
