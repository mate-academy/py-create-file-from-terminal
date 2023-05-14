import os
from typing import Optional
from datetime import datetime


def create_file(file_name: str, destination: Optional[list] = None) -> None:
    if destination is None:
        destination = [""]
    with open(os.path.join(*destination, file_name), "a") as source_file:
        source_file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "\n")
        while True:
            new_str = input("Enter: ")
            if new_str == "stop":
                source_file.write("\n")
                break
            source_file.write(new_str + "\n")


def create_dir(cmd: list[str]) -> list:
    if "-f" in cmd:
        dir_list = [
            cmd[i] for i in range(cmd.index("-d") + 1, cmd.index("-f"))
        ]
    else:
        dir_list = [cmd[i] for i in range(cmd.index("-d") + 1, len(cmd))]
    os.makedirs(os.path.join(*dir_list), exist_ok=True)
    return dir_list
