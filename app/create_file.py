import os
import sys
from datetime import datetime


command = sys.argv


def create_file() -> None:
    if "-d" in command:
        index = 2
        while len(command) != 2 and command[index] != "-f":
            os.makedirs(command[index], exist_ok=True)
            os.chdir(command[index])
            index += 1

    if "-f" in command:
        with open(command[-1], "w") as new_file:
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            line_number = 1
            line_input = input("Enter content line: ")
            while line_input != "stop":
                new_file.write(f"{line_number} {line_input} \n")
                line_number += 1
