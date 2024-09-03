import os
import sys
from datetime import datetime


def create_directory(dirname: str) -> None:
    os.makedirs(dirname, exist_ok=True)


def create_file(filename: str) -> None:
    with open(filename, "a") as f:
        f.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        count = 0
        while True:
            count += 1
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{count} " + line + "\n")


def check_input(input_user: list) -> None:
    command = " ".join(input_user)

    if "-d" in command and "-f" not in command:
        path = os.path.join(*command.split("-d")[1].strip().split())
        create_directory(path)

    if "-d" not in command and "-f" in command:
        name = command.split("-f")[1].strip()
        create_file(name)

    if "-d" in command and "-f" in command:
        path = (os.path.join(*command
                             .split("-d")[1]
                             .split("-f")[0]
                             .strip()
                             .split()))
        name = command.split("-f")[1].split()[0].strip()
        file_path = os.path.join(path, name)
        create_directory(path)
        create_file(file_path)


check_input(sys.argv)
