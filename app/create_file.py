import os
import sys
from datetime import datetime

argv = sys.argv


def create_file(commands: list) -> None:
    flags = ["-d", "-f"]

    if commands[1] not in flags:
        raise ValueError(f"{commands[1]} not a flag!")

    dir_path = None

    position = 1
    while position < len(commands):
        if commands[position] == "-d":
            position += 1
            folder_names = []

            while (position < len(commands)
                   and not commands[position].startswith("-")):
                folder_names.append(commands[position])
                position += 1

            if not folder_names:
                raise ValueError("After '-d' mast be at least 1 folder name")

            dir_path = os.path.join(*folder_names)
            os.makedirs(dir_path, exist_ok=True)

        if position >= len(commands):
            continue

        if commands[position] == "-f":
            position += 1

            if position >= len(commands) or commands[position].startswith("-"):
                raise ValueError("After '-f' mast be a file name")

            if dir_path:
                file_path = os.path.join(dir_path, commands[position])
                f_argument(file_path)
            else:
                f_argument(commands[position])

            position += 1


def f_argument(file_name: str) -> None:
    if not file_name:
        raise ValueError("File name not provided")

    with open(file_name, "a") as file:
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        line = 0
        while True:
            line += 1
            input_data = input("Enter content line:")
            if input_data == "stop":
                break
            file.write(f"\n {line} {input_data}")


if len(argv) > 1:
    create_file(argv)
else:
    print("No argument's provided")
