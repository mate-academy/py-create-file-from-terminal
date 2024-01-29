import os
import sys
from datetime import datetime

commands = sys.argv
dir_path = ""


def make_dir() -> None:

    try:
        directories = commands[commands.index("-d") + 1:commands.index("-f")]
    except ValueError:
        directories = commands[commands.index("-d") + 1:]
    if not directories:
        directories = commands[commands.index("-d") + 1:]

    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)


def make_file() -> None:
    with open(os.path.join(dir_path, commands[commands.index("-f") + 1]), "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        content = input("Enter content line:")
        line_counter = 1
        while content != "stop":
            f.write(f"{line_counter} {content}\n")
            content = input("Enter content line:")
            line_counter += 1


for command in commands:
    if command == "-d":
        make_dir()
    elif command == "-f":
        make_file()
