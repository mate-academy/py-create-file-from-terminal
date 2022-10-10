import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        num = 0
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        content = input("Enter content line: ")
        while content != "stop":
            f.write(f"{num + 1} {content} \n")
            content = input("Enter content line: ")


def create_file_from_terminal() -> None:
    command = sys.argv
    if "-f" not in command and "-d" in command:
        for i in range(2, len(command) - 1):
            os.makedirs(command[i])
    if "-d" not in command and "-f" in command:
        create_file(command[-1])
    if "-d" in command and "-f" in command:
        for i in range(2, len(command) - 1):
            os.makedirs(command[i])
        create_file(command[-1])
