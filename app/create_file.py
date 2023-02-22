import os
import sys
from datetime import datetime

command = sys.argv


def create_file(command: list) -> None:

    if command[1] == "-f":
        open_file(command, "-f")

    if command[1] == "-d" and "-f" in command:
        path = "/".join(command[2:-2])
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, command[-2])
        open_file(file_path, "-d-f")

    if command[1] == "-d":
        os.makedirs("/".join(command[2:]))


def open_file(command, flag):

    if flag == "-f":
        with open(command[2], "w") as file:
            write_file(file)

    if flag == "-d-f":
        with open(command[-2], "w") as file:
            write_file(file)



def write_file(file):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(timestamp + '\n')
    line_number = 1
    while True:
        line_content = input("Enter content line: ")
        if line_content == "stop":
            break
        file.write(f"{line_number} {line_content}\n")
        line_number += 1


if __name__ == '__main__':
    create_file(command)
