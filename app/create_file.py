from datetime import datetime
from sys import argv
from os import path, makedirs
from typing import List


def command_reader(command: tuple) -> str:
    file_name = "file.txt"
    dir_path = None

    if "-d" in command and "-f" in command:
        _, _, *dir, _, file_name = command
        dir_path = path.join(*dir)
        file_name = path.join(dir_path, file_name)
    elif "-d" in command:
        _, _, *dir = command
        dir_path = path.join(*dir)
    elif "-f" in command:
        _, _, file_name = command

    if dir_path:
        makedirs(dir_path, exist_ok=True)

    return file_name


def io_handker(file_exist: bool) -> list:
    output_data = []
    comment = "Line"

    if file_exist:
        comment = "Another line"
    else:
        output_data.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    line_number = 0

    while True:
        line_number += 1
        line = input(f"Enter content line: {comment}{line_number} ")
        if line == "stop":
            break
        output_data.append(f"{comment}{line_number}  {line}\n")

    return output_data


def file_handler(file_name: str, data: List[str]) -> None:

    with open(file_name, "a") as file_out:
        file_out.writelines(data)


def main() -> None:
    file_from_terminal = command_reader(argv)
    data = io_handker(path.exists(file_from_terminal))
    file_handler(file_from_terminal, data)


if __name__ == "__main__":
    main()
