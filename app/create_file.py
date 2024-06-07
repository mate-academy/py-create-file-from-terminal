import sys
import os
import datetime


def create_dirs(dirs: list) -> None:
    path = os.path.join(*dirs)
    if not os.path.exists(path):
        os.makedirs(path)


def write_file(commands: list, anchor_d: bool) -> None:
    directory = commands[-1]
    if anchor_d:
        path = commands[1: commands.index("-f")]
        create_dirs(path)
        path += commands[-1:]
        directory = os.path.join(*path)
    with open(directory, "a") as file:
        date = datetime.datetime.now()
        file.write(f"{date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        page_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{page_number} {line}\n")
            page_number += 1
        file.write("\n")


commands = sys.argv[1:]

if commands[0] == "-d" and not commands.count("-f"):
    create_dirs(commands[1:])
elif commands[0] == "-f":
    write_file(commands, False)
else:
    write_file(commands, True)
