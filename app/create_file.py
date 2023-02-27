from datetime import datetime

import os
import sys


command = sys.argv


def create_file() -> None:
    if "-d" in command:
        index = 2
        while len(command) != 2 and command[index] != "-f":
            os.mkdir(command[index])
            os.chdir(command[index])
            index += 1

    if "-f" in command:
        with open(command[-1], "w") as new_file:
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            line_number = 1
            while True:
                line_input = input("Enter content line: ")
                if line_input == "stop":
                    break
                new_file.write(f"{line_number} {line_input} \n")
                line_number += 1
