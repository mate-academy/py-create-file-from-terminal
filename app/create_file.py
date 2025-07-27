import os
import sys
from datetime import datetime


def create_dir(path: list[str]) -> None:
    current_path = ""
    for folder in path:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            os.mkdir(current_path)


def create_file_by_path(path: list, filename: str) -> None:
    file_path = os.path.join(*path, filename)
    if os.path.exists(file_path):
        return
    with open(file_path, "w"):
        return


def create_file_in_current_dir(filename: str) -> None:
    if os.path.exists(filename):
        return
    with open(filename, "w"):
        return


def write_to_file(path: str, filename: str) -> None:
    file_path = os.path.join(path, filename)
    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                f.write("\n")
                break
            f.write(line)


def execute_command(command: list) -> None:
    if len(command) < 3:
        return

    path = "."
    if "-d" in command:
        path = command[command.index("-d") + 1:-2]
        create_dir(path)

    if "-f" in command:
        if path:
            create_file_by_path(path, command[-1])
            path = os.path.join(".", *path)

        else:
            create_file_in_current_dir(command[-1])

        write_to_file(path, command[-1])


if __name__ == "__main__":
    execute_command(sys.argv[1:])
