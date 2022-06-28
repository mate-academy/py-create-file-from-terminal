import os
import sys

from datetime import datetime

# Parse command line
command_line = sys.argv
directories = []
flags = ""
filename = ""
path = os.getcwd()
if "-f" in command_line and "-d" in command_line:
    directories = command_line[2:-2]
    filename = command_line[-1]
    flags = "df"
elif "-d" in command_line:
    directories = command_line[2:]
    flags = "d"
elif "-f" in command_line:
    filename = command_line[-1]
    flags = "f"

# Create directories
if "d" in flags:
    for directory in directories:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.makedirs(path)

# Create and write file
path_to_file = os.path.join(path, filename)
if "f" in flags:
    with open(path_to_file, "a") as f:
        line = ""
        line_number = 1
        now = datetime.now()
        f.write(f'{now.strftime("%Y-%m-%d %H:%M:%S")}\n')
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1
        f.write("\n")
