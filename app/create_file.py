import sys
import os
import datetime


def create_path(direct: list) -> str:
    path_of_dir = os.path.join(*direct)
    return path_of_dir


def create_file(name_of_file: str) -> None:
    line_of_text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    line_number = 1
    while True:
        input_text = input("Enter line of content: ")
        if input_text == "stop":
            line_of_text += "\n"
            break
        line_of_text += f"{line_number} {input_text}\n"
        line_number += 1

    with open(name_of_file, "a") as result_file:
        result_file.write(line_of_text)


command = sys.argv

if "-d" in command and "-f" in command:
    direct = command[command.index("-d") + 1: command.index("-f")]
    path = create_path(direct)
    file_name = "".join(command[command.index("-f") + 1:])
    os.makedirs(path, exist_ok=True)
    full_file_name = os.path.join(path, file_name)

    create_file(full_file_name)

elif "-d" in command:
    direct = command[command.index("-d") + 1:]
    path = create_path(direct)
    os.makedirs(path, exist_ok=True)

elif "-f" in command:
    file_name = "".join(command[command.index("-f") + 1:])
    create_file(file_name)
