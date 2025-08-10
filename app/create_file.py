import os.path
from sys import argv
from os import getcwd
from os import makedirs
from datetime import datetime

length = len(argv)
command_line = [element for element in argv]
tail_dir = []


def body_function() -> None:
    if "-d" in command_line and "-f" in command_line:
        tail_dir.extend(command_line[2: 4])
        os.chdir(make_directories())
        make_file()

    else:
        if length == 3 and command_line[1] == "-f":
            make_file()

        if command_line[1] == "-d":
            tail_dir.extend(command_line[2: 4])
            make_directories()


def make_directories() -> str:
    full_path = os.path.join(getcwd(), *tail_dir)

    if not os.path.exists(full_path):
        makedirs(full_path)
    return full_path


def make_file() -> None:
    text_of_file = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
    counter = 1
    while True:
        line = input("Enter content line:")

        if line == "stop":
            text_of_file += "\n"
            break

        text_of_file += f"{str(counter)} {line}\n"
        counter += 1

    with open(os.path.join(getcwd(), "file.txt"), "a+") as f:
        f.write(text_of_file)


body_function()
