import sys
import os
import datetime

command = sys.argv
path = os.path.join(*(command[2:]))
path_for_2_flags = os.path.join(*(command[2:-2]))


def create_dirs() -> None:
    if not os.path.exists(path_for_2_flags):
        if "-f" in command:
            os.makedirs(path_for_2_flags)
        else:
            os.makedirs(path)


def create_file() -> None:
    if "-d" in command:
        os.chdir(path_for_2_flags)
    with open(command[-1], "a") as new_file:
        new_file.write(datetime.datetime.now()
                       .strftime("%Y-%m-%d %H:%M:%S") + "\n")
        index = 0
        while True:
            index += 1
            text = input("Enter content line:")
            if text == "stop":
                break
            new_file.write(f"{index} {text}\n")
        new_file.write("\n")


if "-d" in command:
    create_dirs()

if "-f" in command:
    create_file()
