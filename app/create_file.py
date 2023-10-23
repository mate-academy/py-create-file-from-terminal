from datetime import datetime
from sys import argv
from os import path, makedirs


file_name = "file.txt"
dir_path = None

_, *command = argv

if "-d" in command and "-f" in command:
    dir_path, file_name = "/".join(command[1:]).split("-f")
    file_name = path.dirname(dir_path) + file_name

elif "-d" in command:
    dir_path = "/".join(command[1:])

elif "-f" in command:
    _, file_name = command

output_data = []
comment = "Line"

if path.exists(file_name):
    comment = "Another line"
    with open(file_name, "r") as file:
        output_data = file.readlines()
else:
    output_data.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

line_number = 0

while True:
    line_number += 1
    line = input(f"Enter content line: {comment}{line_number} ")
    if line == "stop":
        break
    output_data.append(f"{comment}{line_number}  {line}\n")

if dir_path:
    makedirs(path.dirname(dir_path), exist_ok=True)

with open(file_name, "w+") as f:
    f.writelines(output_data)
