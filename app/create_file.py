import os
import sys
from datetime import datetime


command = sys.argv
dir_path = ""

if "-d" in command:

    try:
        directories = command[2:command.index("-f")]
    except ValueError:
        directories = command[2:]

    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)


if "-f" in command:
    with open(os.path.join(dir_path, command[-1]), "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = input("Enter content line:")
        while line != "stop":
            f.write(line + "\n")
            line = input("Enter content line:")
