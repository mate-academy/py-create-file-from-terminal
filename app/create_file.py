import datetime
import os
import sys


def handle_file(file_name: str) -> None:
    num_of_line = 0
    content = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    while True:
        num_of_line += 1
        line = input("Enter content line: ")
        if line == "stop":
            break
        content += f"{num_of_line} {line}\n"
    content += "\n"

    with open(file_name, "a") as file:
        file.write(content)


def create_file(command: list) -> None:
    if "-d" in command:
        directory_path = command[command.index("-d") + 1:]
        if "-f" in command:
            directory_path = directory_path[:-2]

        path = os.path.join(*directory_path)

        if path:
            os.makedirs(path, exist_ok=True)

    if "-f" in command:
        file_name = command[command.index("-f") + 1]
        handle_file(file_name)


if __name__ == "__main__":
    commands = sys.argv
    create_file(commands)
