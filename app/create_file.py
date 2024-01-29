import os
import sys
from datetime import datetime


command = sys.argv
dir_path = ""

if "-d" in command:
    directories = (
        command[2:command.index("-f")]
        if "-f" in command else command[2:]
    )
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in command:
    file_path = os.path.join(dir_path, command[-1])

    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = input("Enter code line:")
        while line != "stop":
            f.write(line + "\n")
            line = input("Enter content line: ")
