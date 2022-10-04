import os
import sys

from datetime import datetime


def get_commands(key: str) -> str:
    commands = {
        "-d": None,
        "-f": None,
    }
    for i, char in enumerate(sys.argv[1:]):
        if char in commands:
            while i + 1 >= len(sys.argv) or sys.argv[i + 1] in commands:
                commands[char] = sys.argv[i + 2]
                i += 1
    return commands.get(key)


def create_path() -> str:
    path = os.path.join(get_commands("-d"))
    os.makedirs(path, exist_ok=True)
    return path


def create_file() -> None:
    with open(get_commands("-f"), "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = input("Enter content line: ")
        row = 1
        while line.lower() != "stop":
            new_file.write(f"{row} {line}\n")
            row += 1
            line = input("Enter content line: ")


def create_file_from_terminal() -> None:
    if get_commands("-d") is not None and get_commands("-f") is not None:
        os.chdir(create_path())
        create_file()
    elif get_commands("-d") is not None:
        create_path()
    elif get_commands("-f") is not None:
        create_file()
    else:
        print(
            "Enter the command with flag '-d' - create directory,"
            "with flag '-f' - create file or with both of them"
        )


create_file_from_terminal()
