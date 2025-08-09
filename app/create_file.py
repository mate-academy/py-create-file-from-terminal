import os
import sys
from daytime import daytime


command = sys.argv
directories_to_do = "app/"
all_content = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"
line_count = 1
if command[1] == "-d":

    if "-f" in command:
        f_index = command.index("-f")
        for dir in command[2: f_index]:
            directories_to_do += f"{dir}/"
        os.makedirs(directories_to_do, exist_ok=True)

        name = command[f_index + 1]
        if os.path.isfile(name):
            content = "\n" + input("Enter content line: ")
            while content != "stop":
                all_content += f"{line_count} {content}\n"
                content = input("Enter content line: ")
                line_count += 1
            with open(name, "a") as f:
                f.write(all_content)

        else:
            content = input("Enter content line: ")
            while content != "stop":
                all_content += f"{line_count} {content}\n"
                content = input("Enter content line: ")
                line_count += 1
            with open(name, "w") as f:
                f.write(all_content)

    else:
        for dir in command[2:]:
            directories_to_do += f"{dir}/"
        os.makedirs(directories_to_do, exist_ok=True)

if command[1] == "-f":
    name = command[2]

    if os.path.isfile(name):
        content = "\n" + input("Enter content line: ")
        while content != "stop":
            all_content += f"{line_count} {content}\n"
            content = input("Enter content line: ")
            line_count += 1
        with open(name, "a") as f:
            f.write(all_content)

    else:
        content = input("Enter content line: ")
        while content != "stop":
            all_content += f"{line_count} {content}\n"
            content = input("Enter content line: ")
            line_count += 1
        with open(name, "w") as f:
            f.write(all_content)
