import os
import sys
from datetime import datetime


command = sys.argv
directories_to_do = ""
all_content = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"
line_count = 1
if command[1] == "-d":

    if "-f" in command:

        f_index = command.index("-f")
        directories_to_do = os.path.join(command[2: f_index])
        os.makedirs(directories_to_do, exist_ok=True)

        name = os.path.join(directories_to_do, command[f_index + 1])
        if os.path.isfile(name):
            content = "\n" + input("Enter content line: ")
            while content != "stop":
                all_content += f"{line_count} {content}\n"
                content = input("Enter content line: ")
                line_count += 1
            with open(f"{directories_to_do}{name}", "a") as f:
                f.write(all_content)

        else:
            content = input("Enter content line: ")
            while content != "stop":
                all_content += f"{line_count} {content}\n"
                content = input("Enter content line: ")
                line_count += 1
            with open(f"{directories_to_do}{name}", "w") as f:
                f.write(all_content)

    else:
        directories_to_do = os.path.join(command[2:])
        os.makedirs(directories_to_do, exist_ok=True)

if command[1] == "-f":

    name = os.path.join(directories_to_do, command[2])

    if os.path.isfile(name):
        content = "\n" + input("Enter content line: ")
        while content != "stop":
            all_content += f"{line_count} {content}\n"
            content = input("Enter content line: ")
            line_count += 1
        with open(f"{directories_to_do}{name}", "a") as f:
            f.write(all_content)

    else:
        content = input("Enter content line: ")
        while content != "stop":
            all_content += f"{line_count} {content}\n"
            content = input("Enter content line: ")
            line_count += 1
        with open(f"{directories_to_do}{name}", "w") as f:
            f.write(all_content)
