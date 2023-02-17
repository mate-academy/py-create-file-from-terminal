from datetime import datetime
import os.path
import sys

command_line = sys.argv

path_to_file = ""
file_name = ""


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_file(file_name: str, flag: bool) -> None:
    content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    line_number = 1
    while True:
        print_line = input("Enter content line: ")
        if print_line == "stop":
            content += "\n"
            break
        content += f"{line_number} {print_line}\n"
        line_number += 1

    with open(file_name, "w" if flag is False else "a") as file_out:
        file_out.write(content)


def create_directory(directories: list) -> str:
    path_to_file = create_path(directories)

    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)
    return path_to_file


if "-d" in command_line and "-f" not in command_line:
    directories = (command_line[command_line.index("-d") + 1:])
    create_directory(directories)

if "-f" in command_line and "-d" not in command_line:
    file_name = "".join(command_line[command_line.index("-f") + 1:])
    flag = True if os.path.isfile(f"./{file_name}") else False
    create_file(file_name, flag)

if "-d" in command_line and "-f" in command_line:
    directories = (command_line[command_line.index("-d")
                                + 1:command_line.index("-f")])
    file_name = "".join(command_line[command_line.index("-f") + 1:])
    full_name = f"{create_directory(directories)}/{file_name}"

    flag = True if os.path.isfile(f"{full_name}") else False
    create_file(full_name, flag)
