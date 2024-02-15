import os
import sys
from datetime import datetime


arguments = sys.argv
file_name = ""
joined_path = ""

if "-b" in arguments:
    path = []
    for argument in arguments[2:]:
        if argument == "-f":
            break
        path.append(argument)

    joined_path = os.path.join(*path)
    if not os.path.exists(joined_path):
        os.makedirs(joined_path)

if "-f" in arguments:
    file_name = arguments[-1]

    with open(os.path.join(joined_path, file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1
        file.write("\n")
