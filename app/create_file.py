import os
from sys import argv
from datetime import datetime
from typing import List


def get_path() -> None:
    command: List[str] = argv
    path = ""
    if "-d" in command:
        d_index = command.index("-d")
        if "-f" not in command:
            for dir_name in command[(d_index + 1):]:
                path = os.path.join(path, dir_name)
            os.makedirs(path, exist_ok=True)
        else:
            for dir_name in command[(d_index + 1): command.index("-f"):]:
                path = os.path.join(path, dir_name)
            os.makedirs(path, exist_ok=True)
            create_file(os.path.join(path, command[-1]))
    if "-f" in command and "-d" not in command:
        create_file(command[-1])
    return


def create_file(file_name: str) -> None:
    timestamp = datetime.now()
    with open(file_name, "a") as file:
        file.write(timestamp.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        i = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                print(f"The file {file_name} has "
                      f"been created successfully!")
                return
            file.write(str(i) + " " + line + "\n")
            i += 1


get_path()
