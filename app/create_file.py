import sys
import os
import datetime


def make_directory(path):
    os.makedirs(path)


def file_creator(name):
    with open(f"{name}", "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{counter} {content}\n")
            counter += 1


def create_file():

    parsed_commands = sys.argv

    if "-d" in parsed_commands and "-f" in parsed_commands:

        path = "/".join(parsed_commands[2:-2])
        file_name = parsed_commands[-1]

        make_directory(path)
        file_creator(path + "/" + file_name)

    elif "-d" in parsed_commands:

        path = "/".join(parsed_commands[2:])

        make_directory(path)

    elif "-f" in parsed_commands:

        file_name = parsed_commands[-1]

        file_creator(file_name)


create_file()
