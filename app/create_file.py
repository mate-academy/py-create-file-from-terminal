import sys

import os

import datetime


def create_file_function(arguments: list) -> None:
    name = "file.txt"
    if len(arguments) > 4:
        name = os.path.join(arguments[2], arguments[3], arguments[5])
    with open(name, "a") as file:
        current_time = datetime.datetime.now()
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            command = input("Enter content line: ")
            if command != "stop":
                file.write(str(count) + " " + command + "\n")
            if command == "stop":
                break
            count += 1


def create_dir_function(arguments: list) -> None:
    os.mkdir(arguments[2])
    os.mkdir(os.path.join(arguments[2], arguments[3]))


args = sys.argv
if "-d" in args and "-f" not in args:
    create_dir_function(args)
if "-f" in args and "-d" not in args:
    create_file_function(args)
if "-f" in args and "-d" in args:
    create_dir_function(args)
    create_file_function(args)
