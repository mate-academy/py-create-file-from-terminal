import os
import sys
from datetime import datetime

command = sys.argv

if "-d" in command:
    start = command.index("-d") + 1
    if "-f" in command:
        end = command.index("-f")
        filename = command[command.index("-f") + 1]
        directories = os.path.join(*command[start: end])
        path = os.path.join(directories, filename)
    else:
        directories = os.path.join(*command[start:])
    os.makedirs(directories)
if "-f" in command:
    if "-d" not in command:
        path = command[command.index("-f") + 1]
    if os.path.isfile(path):
        mode = "a"
    else:
        mode = "w"
    with open(path, mode) as file:
        now = datetime.now()
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_content = None
        count = 1
        while line_content != "stop":
            line_content = input("Enter content line:")
            if line_content != "stop":
                file.write(f"{count} {line_content}\n")
                count += 1
            else:
                file.write("\n")
        del count
