import sys
import os
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    mark_d = "-d"
    mark_f = "-f"
    if mark_d in command and mark_f in command:
        path = os.path.join(*command[2:command.index(mark_f)])
        os.makedirs(path)
    if mark_d in command:
        path = os.path.join(*command[2:])
        os.makedirs(path)
    elif mark_f in command:
        make_file(command[-1])


def make_file(file_name: str) -> None:
    line = 1
    with open(file_name, "w") as file:
        file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S\n"))
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line} {content}\n")
            line += 1