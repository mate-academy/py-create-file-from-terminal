import sys
import os
import datetime


def create_dirs(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


def write_file(commands: list, anchor_d: bool) -> None:
    directory = commands[-1]
    if anchor_d:
        path = commands[1: commands.index("-f")]
        create_dirs(path)
        path += commands[-1:]
        directory = os.path.join(*path)
    with open(directory, "a") as file:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date}\n")
        page_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{page_number} {line}\n")
            page_number += 1
        file.write("\n")


if __name__ == "__main__":
    commands = sys.argv[1:]
    if commands[0] == "-d" and not commands.count("-f"):
        create_dirs(commands[1:])
    elif commands[0] == "-f":
        write_file(commands, False)
    else:
        write_file(commands, True)
