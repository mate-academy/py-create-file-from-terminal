import os
import sys

from datetime import datetime


command = sys.argv


def create_file(command: list) -> None:

    if command[1] == "-f":
        open_file(command[-1])

    if command[1] == "-d" and "-f" in command:
        path = os.path.join(*command[2:-2])
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, command[-1])
        open_file(file_path)

    if command[1] == "-d" and "-f" not in command:
        os.makedirs(os.path.join(*command[2:]))


def open_file(command: str) -> None:
    with open(command, "w") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


if __name__ == "__main__":
    create_file(command)
