import os

from datetime import datetime
from sys import argv

arguments = argv


def creating_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(line + "\n")


if "-f" in arguments:
    flag_index = arguments.index("-f")

    if "-d" in arguments:
        arguments.pop(flag_index)
        os.makedirs(os.path.join(*arguments[2:-1]))
        creating_file(os.path.join(*arguments[2:]))

    else:
        creating_file(arguments[flag_index + 1])

elif "-d" in arguments:
    os.makedirs(os.path.join(*arguments[2:]))

else:
    raise ValueError("You can use either '-f' or '-d' flags!")
