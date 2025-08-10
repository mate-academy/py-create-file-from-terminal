import datetime
import sys
import os
from typing import TextIO


command = sys.argv


def writer(file_data: TextIO) -> None:
    current_date = (datetime.datetime.now())
    file_data.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    counter = 0
    while True:
        counter += 1
        sentence = input("Enter content line: ")
        if sentence == "stop":
            file_data.write("\n")
            break
        file_data.write(f"{counter} {sentence}\n")


def create_file() -> None:
    file_name = command[command.index("-f") + 1]
    with open(file_name, "a") as file_data:
        writer(file_data)


def create_dir_with_file() -> None:
    d_index = command.index("-d")
    if "-f" in command:
        f_index = command.index("-f")
        path_elements = command[d_index + 1:f_index]
    else:
        path_elements = command[d_index + 1:]

    path = os.path.join(*path_elements)
    if not os.path.exists(path):
        os.makedirs(path)

    if "-f" in command:
        file_name = command[command.index("-f") + 1]
        with open(os.path.join(path, file_name), "a") as file_data:
            writer(file_data)


def main() -> None:
    if "-f" in command and "-d" not in command:
        create_file()

    if "-d" in command:
        create_dir_with_file()


main()
