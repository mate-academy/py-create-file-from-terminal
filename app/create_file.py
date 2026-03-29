import os
import sys
from datetime import datetime


commands = sys.argv
path = []
file_name = ""
permission_create_file = False

if commands:
    for index, part in enumerate(commands):
        if part == "-d":
            for word in commands[(index + 1):]:
                if word == "-f":
                    break
                path.append(word)
            path = os.path.join(*path)
            if not os.path.exists(path):
                os.makedirs(path)

        if part == "-f":
            file_name = commands[(index + 1)]
            permission_create_file = True

    if permission_create_file:
        if path:
            file_path = os.path.join(path, file_name)
        else:
            file_path = file_name

        exists_file = False
        if os.path.exists(file_path):
            exists_file = True

        with open(file_path, "a") as file:
            if exists_file:
                file.write("\n")
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(time + "\n")

            line_number = 0
            while 1:
                line_number += 1
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{line_number} {text}\n")
