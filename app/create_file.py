import sys
import os
from datetime import datetime


def create_file():
    command = sys.argv
    flag_d = "-d"
    flag_f = "-f"
    if flag_d in command and flag_f in command:
        path = os.path.join(*command[2:command.index(flag_f)])
        os.makedirs(path)
    if flag_d in command:
        path = os.path.join(*command[2:])
        os.makedirs(path)
    elif flag_f in command:
        make_file(command[-1])


def make_file(file_name) -> None:
    line = 1
    with open(file_name) as file:
        file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S\n"))
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line} {content}\n")
            line += 1
