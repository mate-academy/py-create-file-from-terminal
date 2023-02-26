import datetime

import os
import sys


command = sys.argv
directory = os.getcwd()

if "-d" in command:
    for line in range(2, len(command)):
        if command[line] == "-f":
            break
        directory = os.path.join(directory, command[line])
    os.mkdir(directory)

if "-f" in command:
    current_file = os.path.join(directory, command[-1])
    with open(current_file, "w") as new_file:
        new_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_number = 1
        while True:
            line_input = input("Enter content line: ")
            if line_input == "stop":
                break
            new_file.write(f"{line_number} {line_input} \n")
            line_number += 1
