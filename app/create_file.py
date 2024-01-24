from sys import argv
from os import path, makedirs
from datetime import datetime


def file_path(arguments: list) -> str:
    return path.join(*arguments)


def create_directory(arguments: list) -> None:
    makedirs(file_path(arguments), exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        line_number = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    command = argv
    if ("-d" in command) and ("-f" not in command):
        create_directory(command[2:])
    elif ("-f" in command) and ("-d" not in command):
        create_file(command[2])
    elif ("-d" in command) and ("-f" in command):
        arguments = [arg for arg in command[2:] if arg != "-f"]
        create_directory(arguments[:-1])
        create_file(file_path(arguments))
    else:
        raise ValueError("Available commands: '-d' and '-f'")


if __name__ == "__main__":
    main()
