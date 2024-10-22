import sys
import os
from datetime import datetime


command = sys.argv
path_parts = command[2:] if "-f" not in command else command[2:-2]
file_name = command[-1] if "-f" in command else ""


def create_dir() -> None:
    if not os.path.exists(os.path.join(*path_parts)):
        os.makedirs(os.path.join(*path_parts))


def create_file() -> None:
    if "-d" in command:
        os.chdir(os.path.join(*path_parts))
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{line_num} {line}\n")
            line_num += 1


if __name__ == "__main__":
    if "-d" in command:
        create_dir()

    if "-f" in command:
        create_file()
