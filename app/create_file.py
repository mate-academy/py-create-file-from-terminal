import os
import sys
from datetime import datetime


def write_contents_to_file(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        line_number = 1

        while (line_content := input("Enter content line: ")) != "stop":
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


def create_file() -> None:
    input_command = sys.argv

    if "-d" in input_command and "-f" in input_command:
        path = os.path.join(*input_command[2:-2])
        os.makedirs(path, exist_ok=True)
        write_contents_to_file(input_command[-1])

    if "-f" not in input_command:
        path = os.path.join(*input_command[-2:])
        os.makedirs(path, exist_ok=True)

    if "-d" not in input_command:
        write_contents_to_file(input_command[-1])
