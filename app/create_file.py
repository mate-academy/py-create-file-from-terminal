import os
import sys
from datetime import datetime

command = sys.argv[1:]

is_directory = False
is_file = False
path = []
file_name = ""

for i in range(len(command)):
    if command[i] == "-f":
        is_file = True
        file_name = command[i + 1]
        break
    if is_directory:
        path.append(command[i])
    if command[i] == "-d":
        is_directory = True

directory_way = os.path.join(path[0])

if len(path) > 1:
    directory_way = path[0]
    for index in range(len(path) - 1):
        directory_way = os.path.join(directory_way, path[index + 1])

if not os.path.exists(directory_way):
    os.makedirs(directory_way)

if is_file:
    file_path = file_name
    if directory_way:
        file_path = os.path.join(directory_way, file_name)

    mode = "w"
    if os.path.exists(file_path):
        mode = "a"

    with open(file_path, mode) as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")

        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{count} {line}\n")
            count += 1
