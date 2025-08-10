import os
import sys
from datetime import datetime


def create_directories(path: list):
    previous_directories = ""
    for directory in path:
        if previous_directories == "":
            os.mkdir(directory)
            previous_directories = previous_directories + directory + "/"
        else:
            os.mkdir(previous_directories + directory)
            previous_directories = previous_directories + directory + "/"
    return previous_directories


def getting_commands(command: list):
    if "-d" in command and "-f" in command:
        directory_command = command.index("-d")
        file_command = command.index("-f")
        directory_names = command[directory_command + 1:file_command]
        file_name = command[file_command + 1:]
        path = create_directories(directory_names)
        writing_in_the_file(file_name, path)
    elif "-d" in command:
        directory_command = command.index("-d")
        directory_names = command[directory_command + 1:]
        create_directories(directory_names)
    elif "-f" in command:
        file_command = command.index("-f")
        file_name = command[file_command + 1:]
        writing_in_the_file(file_name)


def writing_in_the_file(file_name: list, path=None):
    time = datetime.now()
    str_time = time.strftime("%Y-%m-%d %H:%M:%S")
    file_name = file_name[0]
    text = []
    line = input("Enter content line: ")
    while line != "stop":
        text.append(line)
        line = input("Enter content line: ")

    if path is not None:
        with open(path + "/" + file_name, "a") as file:
            file.write(str_time + "\n")
            [file.write(str(number + 1) + " " + line + "\n") for
             number, line in enumerate(text)]
            file.write("\n")
    else:
        with open(f"app/{file_name}", "a") as file:
            file.write(str_time + "\n")
            [file.write(str(number + 1) + " " + line + "\n")
             for number, line in enumerate(text)]
            file.write("\n")


def main():
    getting_commands(sys.argv)
