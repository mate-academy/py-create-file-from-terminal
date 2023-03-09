import os
import sys
from datetime import datetime


def create_content(path_to_file: str) -> None:
    with open(path_to_file, "w") as f:
        time_now = datetime.now()
        f.write(time_now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        content = input("Enter content line: ")
        line_number = 1
        while content != "stop":
            f.write(str(line_number) + " " + content + "\n")
            content = input("Enter content line: ")
            line_number += 1


def create_file() -> None:
    commands = sys.argv

    if "-d" in commands and "-f" in commands:
        dirs_path = os.path.join(*commands[2:-2])
        os.makedirs(dirs_path, exist_ok=True)

        path_to_file = os.path.join(dirs_path, commands[-1])
        create_content(path_to_file)

    elif "-d" in commands and "-f" not in commands:
        dirs_path = os.path.join(*commands[2:])
        os.makedirs(dirs_path, exist_ok=True)

    elif "-f" in commands and "-d" not in commands:
        path_to_file = commands[-1]
        create_content(path_to_file)


if __name__ == "__main__":
    create_file()
