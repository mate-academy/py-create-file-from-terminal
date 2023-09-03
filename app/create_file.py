import os
import sys
from datetime import datetime


def create_directories(directories: list) -> str:
    for index, item in enumerate(directories):
        if item == "-d":
            directory_list = directories[index + 1:]
            directory = "/".join(directory_list)
    if not os.path.exists(directory):
        os.makedirs(directory)
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
        start = command.index("-d") + 1
        end = command.index("-f")

        path_to_file = create_directories(command[start:end])
        add_content(os.path.join(path_to_file, command[end + 1]))

    elif "-d" in command:
        start = command.index("-d") + 1
        end = len(command)
        create_directories(command[start:end])

    elif "-f" in command:
        index = command.index("-f") + 1
        add_content(command[index])
