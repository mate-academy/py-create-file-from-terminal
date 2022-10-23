import os
import sys
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    if "-f" not in command:
        file_path = os.path.join(*command[2:])
        os.makedirs(file_path, exist_ok=True)
        return
    file_path = ""
    if "-d" in command:
        file_path = os.path.join(*command[2:-2])
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    file_name = os.path.join(file_path, command[-1])

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        line_input = input("Enter content line: ")
        line_number = 1
        while line_input != "stop":
            file.write(f"Line{line_number} {line_input}\n")
            line_input = input("Enter content line: ")
            line_number += 1


create_file()
