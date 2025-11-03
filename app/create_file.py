from os import path, makedirs
from sys import argv
from datetime import datetime


""" Check for flags and list path and file name """


def flags_interpreter(arguments: list) -> list:
    dir_arg, file_arg = False, False
    dir_path, file_name = "", ""
    dir_parts = []
    for argument in arguments:
        if argument == "-d" and not dir_path:
            dir_arg, file_arg = True, False
            continue
        if argument == "-f":
            if not file_name:
                file_arg = True
            dir_arg = False
            continue
        if dir_arg:
            dir_parts.append(argument)
        if file_arg:
            file_name = argument
            file_arg = False
    if dir_parts:
        dir_path = create_path(dir_parts)
    if file_name:
        file_name = create_path([dir_path, file_name])
    return [dir_path, file_name]


""" Create directory path """


def create_path(folders: list) -> str:
    return path.join(*folders)


""" Create folders if not exists """


def create_dir(dir_path: str) -> None:
    if not path.exists(dir_path):
        makedirs(dir_path)


""" Create or update text file """


def create_text_file(file_name: str) -> None:
    lines = [datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")]
    line = ""
    line_counter = 0
    print("Enter file content (type \'stop\' to end the file):")
    while line != "stop":
        line_counter += 1
        line = input("Enter content line: ")
        lines.append(f"{line_counter} {line}") if line != "stop" else None
    lines.append("")
    with open(file_name, "a") as text_file:
        for line in lines:
            text_file.write(f"{line}\n")


""" Main code """

directory, text_file = flags_interpreter(argv)

if directory:
    create_dir(directory)
if text_file:
    create_text_file(text_file)
