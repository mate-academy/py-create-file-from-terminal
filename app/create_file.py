import sys
import os
import datetime


def create_dirs(command: list) -> str:
    d_index, f_index = 2, len(command)
    if "-f" in command:
        f_index -= 2
    dir_path = os.path.join(command[d_index:f_index])
    path = os.path.dirname(dir_path)
    os.makedirs(path, exist_ok=True)
    return path


def write_file(command: list, path: str = "") -> None:
    filename = os.path.join(path, command[-1])
    index = 1
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(time + "\n")
        data = input("Enter content line: ")
        while data != "stop":
            file.write(f"{index} {data}\n")
            index += 1
            data = input("Enter content line: ")


if __name__ == "__main__":
    command = sys.argv
    path = ""
    if "-d" in command:
        path = create_dirs(command)
    if "-f" in command:
        write_file(command, path)
