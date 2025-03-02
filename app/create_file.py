import os
from sys import argv
from pathlib import Path
from datetime import datetime


def get_path() -> None:
    command = argv
    d_index, path = 0, ""
    if "-d" in command:
        d_index = command.index("-d")
        if "-f" not in command:
            path = Path("/".join(command[(d_index + 1):]))
            return path.mkdir(parents=True, exist_ok=True)
        else:
            path = Path("/".join(command[d_index + 1: command.index("-f")]))
            path.mkdir(parents=True, exist_ok=True)
            return create_file(os.path.join(path, command[-1]))
    if "-f" in command and "-d" not in command:
        return create_file(command[-1])


def create_file(file_name: str) -> None:
    timestamp = datetime.now()
    with open(file_name, "a") as file:
        file.write(timestamp.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        i = 1
        while True:
            line = input("Enter content line: ")
            if not line.lower() == "stop":
                file.write(str(i) + " " + line + "\n")
                i += 1
            else:
                print(f"The file {file_name} has created")
                break


get_path()
