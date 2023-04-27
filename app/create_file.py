import os
import sys
import datetime


commands = sys.argv
directory = ""
parent_dir = os.getcwd()
if "-d" in commands:
    if "-f" in commands:
        dirs = commands[commands.index("-d") + 1: commands.index("-f")]
    else:
        dirs = commands[commands.index("-d") + 1:]
    directory = "\\".join(dirs)
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)

if "-f" in commands:
    new_file = commands[commands.index("-f") + 1]

    with open(os.path.join(parent_dir, directory, new_file), "a") as file:

        file.write(str(datetime.datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        text = input("Enter content line: ")
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text} \n")
            text = input("Enter content line: ")
        file.write("\n")
