import os
import sys
import datetime


commands = sys.argv
directory = ""
parent_dir = os.getcwd()
if "-d" in commands:
    if "-f" in commands:
        directory = "\\".join(commands[commands.index("-d") + 1:
                                       commands.index("-f")])
    else:
        directory = "\\".join(commands
                              [commands.index("-d") + 1:])

    path = os.path.join(parent_dir, directory)
    os.makedirs(path)

if "-f" in commands:
    new_file = commands[commands.index("-f") + 1]

    with open(os.path.join(parent_dir, directory, new_file), "a") as f:

        f.write(str(datetime.datetime.now().
                    strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        text = input("Enter content line: ")
        count = 0
        while text != "stop":
            count += 1
            f.write(f"{count} {text} \n")
            text = input("Enter content line: ")
        f.write("\n")
