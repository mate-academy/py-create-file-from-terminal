import sys
import os
from datetime import datetime


index = 0


def create_folders() -> str:
    global index
    index += 1
    path_arr = []

    while terminal_command[index] not in ["-f", "-d"]:
        path_arr.append(terminal_command[index])
        index += 1

    directory_path = os.path.join(*path_arr)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path


def create_file(path: str = "") -> None:
    global index
    index += 1

    path_with_file = os.path.join(path, terminal_command[index])

    with open(path_with_file, "a") as new_file:
        new_file.write(
            str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
        )
        string_number = 1
        string = input()
        while string != "stop":
            new_file.write(f"{str(string_number)} {string} \n")
            string_number += 1
            string = input()


terminal_command = sys.argv[1:]
if terminal_command[index] == "-d":
    path = create_folders()
if terminal_command[index] == "-f":
    create_file(path)
