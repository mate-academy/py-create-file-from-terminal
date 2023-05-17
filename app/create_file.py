from os import makedirs, path
from datetime import datetime
from sys import argv

command = argv


def creating_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(line + "\n")


if "-f" in command:
    if "-d" in command:
        command.pop(command.index("-f"))
        makedirs(path.join(*command[2:-1]))
        creating_file(path.join(*command[2:]))
    else:
        creating_file(command[command.index("-f") + 1])
if "-d" in command:
    makedirs(path.join(*command[2:]))
