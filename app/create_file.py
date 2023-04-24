import sys
import os
from datetime import datetime


def create_dir() -> None:
    input_command = sys.argv
    file_name = ""
    parent_dir = ""
    if ("-f" and "-d") in input_command:
        index_f, index_d = input_command.index("-f"), input_command.index("-d")
        file_name = input_command[index_f + 1]
        if index_d < index_f:
            parent_dir = "/".join(input_command[(index_d + 1):index_f])
        if index_d > index_f:
            parent_dir = "/".join(input_command[index_d + 1:])
    if "-f" not in input_command and "-d" not in input_command:
        print("Please specify at least one flag -f or -d")
        sys.exit(1)
    if "-f" in input_command and "-d" not in input_command:
        file_name = input_command[1]
    if "-d" in input_command and "-f" not in input_command:
        parent_dir = "/".join(input_command[1:])
    path = os.path.join(parent_dir, file_name)
    os.makedirs(path)


def create_file(name_file: str) -> None:
    with open(name_file, "a") as file:
        file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() != "stop":
                file.write(f"{line_number} {line}\n")
                line_number += 1


if __name__ == "__main__":
    create_dir()
