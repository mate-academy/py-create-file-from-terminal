import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        num = 1
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break

            f.write(f"{num} {content} \n")
            num += 1


def create_file_from_terminal() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        for i in range(2, len(command) - 1):
            os.makedirs(command[i])
        create_file(command[-1])
    if "-d" in command:
        for i in range(2, len(command) - 1):
            os.makedirs(command[i])
    if "-f" in command:
        create_file(command[-1])
