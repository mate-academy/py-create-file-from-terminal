import os
import sys
from datetime import datetime


command = sys.argv
dir_path = ""
file_path = ""

if "-f" in command:
    file_index = command.index("-f")
    file_path = os.path.join(*command[file_index + 1:])
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = input("Enter code line:")
        while line != "stop":
            f.write(line + "\n")
            line = input("Enter content line: ")

else:
    if "-d" in command:
        directories = (
            command[2:command.index("-f")]
            if "-f" in command else command[2:]
        )
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
