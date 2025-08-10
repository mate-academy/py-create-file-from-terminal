import os
import sys
from datetime import datetime


def create_directories(directories: list) -> str:
    directory = os.path.join(*directories)
    os.makedirs(directory, exist_ok=True)
    return directory


def add_content(file_name: str) -> None:
    content_list = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    counter = 1
    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break
        counter += 1
        content_list.append(f"{counter} {line}")

    status = "a" if os.path.exists(file_name) else "w"

    with open(file_name, status) as file:
        if status == "a":
            file.write("\n" * 2 + "\n".join(content_list))
        else:
            file.write("\n".join(content_list))


if __name__ == "__main__":
    command = sys.argv

    if "-d" in command and "-f" in command:
        path_to_file = create_directories(
            command[command.index("-d") + 1:command.index("-f")]
        )
        add_content(os.path.join(
            path_to_file, command[command.index("-f") + 1]
        ))

    elif "-d" in command:
        create_directories(command[command.index("-d") + 1:])

    elif "-f" in command:
        add_content(command[command.index("-f") + 1])
