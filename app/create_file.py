import datetime
import os
import sys


# to read the arguments passed in terminal
arguments = sys.argv


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path)


def file_content(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S" + "\n")
        )
        content = input("Enter content line: ")
        line = 1

        while content != "stop":
            file.write(str(line) + " " + content + "\n")
            line += 1
            content = input("Enter content line: ")

        if content == "stop":
            file.write("\n")


if "-f" in arguments and "-d" not in arguments:
    file_name = arguments[-1]
    file_content(file_name)
if "-d" in arguments and "-f" not in arguments:
    d_index = arguments.index("-d")
    directories = arguments[d_index + 1:]
    dir_path = os.path.join(os.getcwd(), *directories)
    create_directory(dir_path)
if "-d" in arguments and "-f" in arguments:
    d_index, f_index = arguments.index("-d"), arguments.index("-f")
    if f_index > d_index:
        directories = arguments[d_index + 1:f_index]
    else:
        directories = arguments[d_index + 1:]
    dir_path = os.path.join(os.getcwd(), *directories)
    create_directory(dir_path)

    file_name = arguments[f_index + 1]
    file_path = os.path.join(dir_path, file_name)
    file_content(file_path)
