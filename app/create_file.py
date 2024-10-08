import sys
import os
import datetime


def create_path_and_file_name(arguments: list) -> None:
    flag = True
    for val in arguments:
        if val == "-f":
            flag = False
        if flag:
            directory.append(val)
        else:
            file_name.append(val)
    directory.pop(0)
    file_name.pop(0)


def create_dir() -> None:
    for direc in directory:
        if not os.path.exists(direc):
            os.mkdir(direc)
        os.chdir(direc)


def write_information_into_file() -> None:
    with open("file_name", "w") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    with open("file_name", "a") as file:
        while True:
            inp = input("Enter content line: ")
            if inp == "stop":
                break
            file.write(inp + "\n")


input_arguments = sys.argv
input_arguments.pop(0)
os.chdir("app")
if "-d" not in input_arguments:
    write_information_into_file()
else:
    directory = []
    file_name = []
    create_path_and_file_name(input_arguments)
    create_dir()
    write_information_into_file()
