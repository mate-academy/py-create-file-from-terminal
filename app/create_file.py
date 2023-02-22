import os
import sys
from datetime import datetime

commands = sys.argv[1:]
commands = " ".join(commands).split("-f")
command_path = commands.pop(0).strip("-d").split()
if command_path:
    path = [folder for folder in command_path]
    path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)
if commands:
    output_file = commands[0].strip()
    with open(output_file, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{line} {content}\n")
            line += 1
