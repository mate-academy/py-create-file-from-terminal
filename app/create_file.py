import os.path
from sys import argv
from os import makedirs
import datetime


def make_dir(directories: list) -> os:
    path = os.path.join("/".join(directories))
    if not os.path.exists(path):
        makedirs(path)
    return path


def write_in_file(filename: str, path: str = "") -> None:
    current_time = datetime.datetime.now()
    if path:
        path += "/"
    with open(f"{path}{filename}", "a") as f:
        f.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            append_line = input("Enter content line: ")
            if append_line == "stop":
                break
            f.write(append_line + "\n")


def create_file_from_terminal(cmd: list) -> None:
    if "-d" in cmd and "-f" in cmd:
        path = make_dir(cmd[cmd.index("-d") + 1:cmd.index("-f")])
        filename = cmd[cmd.index("-f") + 1]
        write_in_file(filename, path)

    if "-d" in cmd and "-f" not in cmd:
        make_dir(cmd[cmd.index("-d") + 1:])

    if "-f" in cmd and "-d" not in cmd:
        filename = "".join(cmd[cmd.index("-f") + 1])
        write_in_file(filename)


create_file_from_terminal(argv)
