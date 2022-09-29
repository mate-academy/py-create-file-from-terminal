from datetime import datetime
import sys
import os


directory = ""
command_list = sys.argv
if command_list[1] == "-d":
    try:
        f_command = command_list.index("-f")
    except ValueError:
        f_command = None
    directory = os.path.join(*command_list[2:f_command])
    if not os.path.exists(directory):
        os.makedirs(directory)

if "-f" in command_list:
    f_index = command_list.index('-f')
    with open(str(os.path.join(directory, command_list[f_index + 1])),
              "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            line = str(input("Enter content line: "))
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
