import sys
import os
from datetime import datetime


def parse_comms() -> tuple:
    command = sys.argv

    if "-f" in command and "-d" in command:
        path_parts = command[2:command.index("-f")]
        file_name = command[command.index("-f") + 1]

    elif "-d" in command:
        path_parts = command[2:]
        file_name = ""

    elif "-f" in command:
        path_parts = []
        file_name = command[command.index("-f") + 1]
    else:
        raise ValueError("invalid command, you should use -d or -f")
    return path_parts, file_name


def create_dir(path_parts: list) -> None:
    if not os.path.exists(os.path.join(*path_parts)):
        os.makedirs(os.path.join(*path_parts))


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{line_num} {line}\n")
            line_num += 1


if __name__ == "__main__":
    path_parts, file_name = parse_comms()

    if path_parts:
        create_dir(path_parts)

    if file_name:
        create_file(file_name)
