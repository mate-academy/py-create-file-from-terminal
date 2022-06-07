import datetime
import sys
import os


def create_full_dir():
    command = sys.argv
    path = os.getcwd()
    if "-d" in command and "-f" in command:
        dirs = command[command.index("-d") + 1: command.index("-f")]
        path = os.path.join(path, *dirs)
        if not os.path.exists(path):
            os.makedirs(path)
        create_file(path, command[-1])
    elif "-d" in command and "-f" not in command:
        dirs = command[command.index("-d") + 1:]
        path = os.path.join(path, *dirs)
        if not os.path.exists(path):
            os.makedirs(path)
    elif "-f" in command and "-d" not in command:
        create_file(path, command[-1])


def create_file(path, name):
    with open(path + "\\" + name, "a+") as file:
        file.write(datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S\n"))
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{content}\n")


create_full_dir()
