import os
import sys
from datetime import datetime

command = sys.argv


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write((datetime.now(). strftime("%Y-%m-%d, %H:%M:%S") + "\n"))
        line_number = 1
        while True:
            line_number += 1
            line_text = input("Enter content line:")
            if line_text == "stop":
                break
            file.write(f"{line_number} {line_text}\n")


def create_directories_and_file() -> None:
    if "-d" in command:
        d_index = command.index("-d")
        f_index = command.index("-f") if "-f" in command else len(command)
        dir_list = command[d_index + 1: f_index]

        dir_path = "/".join(dir_list) + "/"
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""
    if "-f" in command:
        f_index = command.index("-f")
        file_name = command[f_index + 1]
        create_file(dir_path + file_name)
