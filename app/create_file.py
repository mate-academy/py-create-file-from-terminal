import datetime
import os
import sys


def create_file(name: str, path_to_file: str = "") -> None:
    
    with open(path_to_file + name, "w") as file:
        file.write(f"{datetime.datetime.now()}")
        line_number = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line_number} {content}")
            i += 1

command = sys.argv
if "-d" not in command and "-f" in command:
    create_file(command[-1])
if "-d" in command and "-f" not in command:
    path = os.path.join(command[command.index("-d") + 1:])
    os.makedirs(path, exist_ok=True)
if "-d" in command and "-f" in command:
    path = os.path.join(command[command.index("-d") + 1: command.index("-f")])
    os.makedirs(path, exist_ok=True)
    create_file(command[-1], path)
