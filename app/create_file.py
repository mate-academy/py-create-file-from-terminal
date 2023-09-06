import sys
import os
from datetime import datetime


def create_directories(directories: list) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def add_info_to_file(file_name: str) -> None:
    lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{len(lines)} {line}")

    status = "a" if os.path.exists(file_name) else "w"
    with open(file_name, status) as file:
        if status == "a":
            file.write("\n" * 2 + "\n".join(lines))
        else:
            file.write("\n".join(lines))


if __name__ == "__main__":
    command = sys.argv

    if "-d" in command and "-f" in command:
        start = command.index("-d") + 1
        end = command.index("-f")

        path_to_file = create_directories(command[start:end])
        add_info_to_file(os.path.join(path_to_file, command[end + 1]))

    elif "-d" in command:
        start = command.index("-d") + 1
        end = len(command)
        create_directories(command[start:end])

    elif "-f" in command:
        index = command.index("-f") + 1
        add_info_to_file(command[index])
