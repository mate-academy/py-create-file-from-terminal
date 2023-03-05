import sys
import os
from datetime import datetime


terminal_command = sys.argv[1:]
index = 0
path = []

while index < len(terminal_command) - 1:

    if terminal_command[index] == "-d":
        index += 1
        while terminal_command[index] not in ["-f", "-d"]:
            path.append(terminal_command[index])
            index += 1
        path = os.path.join(*path)
        os.makedirs(path, exist_ok=True)

    if terminal_command[index] == "-f":
        index += 1
        path = os.path.join(path, terminal_command[index])
        with open(path, "a") as new_file:
            new_file.write(
                str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
            )
            string_number = 1
            string = input()
            while string != "stop":
                new_file.write(f"{str(string_number)} {string} \n")
                string_number += 1
                string = input()
