import os
import sys
from datetime import datetime


def create_file(filename: str, path: str = "") -> None:
    file_path = os.path.join(path, filename)
    with open(file_path, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_counter = 0
        while True:
            line_counter += 1
            file_input = input("Enter content line (or stop): ")
            if file_input == "stop":
                new_file.write("\n")
                break
            new_file.write(f" {line_counter} {file_input} \n")


def create_directory(*args: list) -> str | bytes:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def operations_with_command() -> None:
    commands = sys.argv
    if "-d" in commands and "-f" in commands:
        path = create_directory(commands[2:-2])
        create_file(commands[-1], path)
    elif "-d" in commands:
        create_directory(commands[2:])
    elif "-f" in commands:
        create_file(commands[-1])


if __name__ == "__main__":
    operations_with_command()
