import sys
import os
import datetime


directory = ""
command_list = sys.argv
if command_list[1] == "-d":
    try:
        f_command = command_list.index("-f")
    except ValueError:
        f_command = None
    os.makedirs("\\".join(command_list[2:f_command]))
    directory = "\\".join(command_list[2:f_command]) + "\\"
if "-f" in command_list:
    with open(f"{directory}{command_list[command_list.index('-f') + 1]}",
              "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            line = str(input("Enter content line: "))
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1
