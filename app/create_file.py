import os
import sys
from datetime import datetime


def create_dir(path: list) -> None:
    for i in range(len(path)):
        if not os.path.exists("\\".join(path[:i + 1])):
            os.mkdir("\\".join(path[:i + 1]))


def create_file_by_path(path: list, filename: str) -> None:
    if os.path.exists("\\".join(path) + "\\" + filename):
        return
    with open("\\".join(path) + "\\" + filename, "w"):
        return


def create_file_in_current_dir(filename: str) -> None:
    if os.path.exists(filename):
        return
    with open(filename, "w"):
        return


def execute_command(command: list) -> None:
    if len(command) < 3:
        return

    path = ""
    if "-d" in command:
        path = command[command.index("-d") + 1:-2]
        create_dir(path)

    if "-f" in command:
        if path:
            create_file_by_path(path, command[-1])
            path = "\\".join(path) + "\\"
        else:
            create_file_in_current_dir(command[-1])
        with open(path + command[-1], "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                f.write(line)


if __name__ == "__main__":
    execute_command(sys.argv)
