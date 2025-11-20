import sys
import os
from datetime import datetime


def make_directory_and_open(directory: list[str]) -> None:
    directory = os.path.join(os.getcwd(), *directory)
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)


def write_file(file_name: str) -> None:
    file_lines = []
    with open(file_name, "a") as file:
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                now = datetime.now()
                formatted = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{formatted}\n")
                for line_number, line in enumerate(file_lines, 1):
                    file.write(f"{line_number} {line}\n")
                file.write("\n")
                break
            file_lines.append(line)


command_line = sys.argv
if "-d" in command_line and "-f" in command_line:
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
