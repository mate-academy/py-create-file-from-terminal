import os
import sys
from datetime import datetime


def create_file_or_append_to_existing(file_name: str, mode: str) -> None:
    f = open(file_name, mode)
    count = 1
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    while True:
        input_str = str(input("Enter content line: "))
        if input_str != "stop":
            f.write(f"{count} {input_str}\n")
        else:
            break
        count += 1
    f.close()


def create_file_from_terminal() -> None:
    command = " ".join(sys.argv[1:])
    commands_from_terminal = command.strip().split("-")
    commands_stripped = []
    dir_path = ""
    file_name = ""
    for command in commands_from_terminal:
        if command:
            commands_stripped.append(command.rstrip())
    if len(commands_stripped) == 1:
        if commands_stripped[0][0] == "d":
            dir_command = commands_stripped[0].split()
            dir_path = f"{'/'.join(dir_command[1:])}"
        if commands_stripped[0][0] == "f":
            file_command = commands_stripped[0].split()
            file_name = "".join(file_command[1:])
    else:
        if commands_stripped[0][0] == "d":
            dir_command = commands_stripped[0].split()
            dir_path = f"{'/'.join(dir_command[1:])}"
        if commands_stripped[1][0] == "f":
            file_command = commands_stripped[1].split()
            file_name = "".join(file_command[1:])
    if dir_path and not file_name:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    if file_name and dir_path:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(f"{dir_path}/{file_name}"):
            create_file_or_append_to_existing(f"{dir_path}/{file_name}", "w")
        else:
            create_file_or_append_to_existing(f"{dir_path}/{file_name}", "a")
    if file_name and not dir_path:
        if not os.path.isfile(file_name):
            create_file_or_append_to_existing(file_name, "w")
        else:
            create_file_or_append_to_existing(file_name, "a")


create_file_from_terminal()
