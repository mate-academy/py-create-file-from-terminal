import os
import sys

from datetime import datetime


def create_content(text: str) -> None:
    with open(text, "a") as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        content = input("Enter content line: ")
        i = 1
        while content != "stop":
            f.write(f"Line{i} {content}\n")
            content = input("Enter content line: ")


def create_file() -> None:
    commands = sys.argv
    if "-f" not in commands:
        path = os.path.join(*commands[2:])
        if not os.path.exists(path):
            os.makedirs(path)
        return
    path = ""
    if "-d" in commands:
        path = os.path.join(*commands[2:-2])
        if not os.path.exists(path):
            os.makedirs(path)
    file_name = os.path.join(path, commands[-1])
    create_content(file_name)


create_file()
