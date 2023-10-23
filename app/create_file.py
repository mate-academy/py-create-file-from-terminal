import datetime
import sys
import os
from typing import IO


def write_to_file(open_file: IO[str]) -> None:
    current_date = (datetime.datetime.now())
    open_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    counter = 0
    while True:
        counter += 1
        sentence = input("Enter content line: ")
        if sentence == "stop":
            open_file.write("\n")
            break
        open_file.write(f"{counter} {sentence}\n")


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file_data:
        write_to_file(file_data)


def create_dir(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def main() -> None:
    command_from_terminal = sys.argv
    file_name = ""
    directory_path = ""

    if "-f" in command_from_terminal:
        f_index = command_from_terminal.index("-f")
        file_name = command_from_terminal[f_index + 1]
        del command_from_terminal[f_index:f_index + 2]

    if "-d" in command_from_terminal:
        directory_path = os.path.join(*command_from_terminal[2:])

    if directory_path:
        create_dir(directory_path)

    if file_name:
        create_file(os.path.join(directory_path, file_name))


main()
