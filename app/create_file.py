from sys import argv
import os
from datetime import datetime


def create_file() -> None:
    command = argv
    flag_d = "-d"
    flag_f = "-f"

    if flag_d in command and flag_f in command:
        path = os.path.join(*command[2:command.index(flag_f)])
        os.makedirs(path)
        make_file(os.path.join(path, command[-1]))

    elif flag_d in command:
        path = os.path.join(*command[2:])
        os.makedirs(path)

    elif flag_f in command:
        make_file(command[-1])


def make_file(name_file: str) -> None:
    line = 1

    with open(name_file, "w") as created_file:
        created_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            created_file.write(f"{line} {content}\n")
            line += 1


create_file()
