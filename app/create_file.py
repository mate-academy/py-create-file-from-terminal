import sys
import os
from datetime import datetime


def make_directory_and_open(directory: list[str]) -> None:
    directory_list = []
    for name in directory:
        directory_list.append(name)
    directory = os.path.join(os.getcwd(), *directory_list)
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)


def write_file(file_name: str) -> None:
    file_lines = []
    with open(file_name, "a") as file:
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                #  add time stamp
                now = datetime.now()
                formatted = now.strftime("%Y-%m-%d %H:%M:%S")
                #  write lines
                file.write(f"{formatted}\n")
                for i, line in enumerate(file_lines, 1):
                    file.write(f"{i} {line}\n")
                file.write("\n")
                break
            file_lines.append(line)


command_line = sys.argv
if "-d" in command_line and "-f" in command_line:
    # make directory and go to
    f_position = 0
    for num in range(len(command_line)):
        if command_line[num] == "-f":
            f_position = num
    make_directory_and_open(command_line[2:f_position])
    write_file(command_line[f_position + 1])


elif "-f" in command_line:
    write_file(command_line[2])
elif "-d" in command_line:
    make_directory_and_open(command_line[2:])
