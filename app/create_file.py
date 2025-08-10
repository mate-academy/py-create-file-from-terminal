import os
import sys
from datetime import datetime


def command_definition(commands: list[str]) -> None:
    if "-f" in commands and "-d" in commands:
        command_d(commands)
        command_f(commands)
    elif "-f" in commands:
        command_f(commands)
    elif "-d" in commands:
        command_d(commands)
    else:
        raise ValueError("No valid flag (-f or -d) provided in the command.")


def command_d(commands: list[str]) -> None:

    parent_dir = os.getcwd()

    for directory in commands[2:]:
        if directory != "-f":
            new_dir = os.path.join(parent_dir, directory)
            os.makedirs(new_dir, exist_ok=True)
            parent_dir = new_dir
        else:
            break


def command_f(commands: list[str]) -> None:

    path = os.path.join("/".join(commands[2:-2]))
    file_path = os.path.join(path, commands[-1])

    with open(file_path, "a") as file:

        if os.stat(file_path).st_size != 0:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        input_line = input("Enter content line: ")
        line_number = 1

        while input_line != "stop":
            output = f"{line_number} {input_line}"
            file.write(output + "\n")
            input_line = input("Enter content line: ")
            line_number += 1


if __name__ == "__main__":
    command_definition(sys.argv)
