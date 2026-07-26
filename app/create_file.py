import os
import sys
from datetime import datetime


catalog = ""
commands = sys.argv

if commands[1] == "-d":
    try:
        f_command = commands.index("-f")
    except ValueError:
        f_command = None
    catalog = os.path.join(*commands[2:f_command])
    if not os.path.exists(catalog):
        os.makedirs(catalog)

if "-f" in commands:
    f_index = commands.index("-f")
    with open(str(os.path.join(catalog, commands[f_index + 1])),
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
