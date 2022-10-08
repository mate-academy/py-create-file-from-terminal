import sys
import os

from datetime import datetime


def make_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 1
        line_content = input("Enter content line: ")
        while line_content.lower() != "stop":
            file.write(f"{line_num} {line_content}\n")
            line_content = input("Enter content line: ")
            line_num += 1


def get_terminal_content() -> None:
    command = sys.argv

    d_index = command.index("-d") if "-d" in command else None
    f_index = command.index("-f") if "-f" in command else None

    if d_index and f_index:
        path = os.path.sep.join(command[d_index + 1: f_index])
        file_name = command[-1]
        os.makedirs(path, exist_ok=True)
        make_file(os.path.join(path, file_name))
    elif d_index:
        path = os.path.sep.join(command[d_index + 1: len(command)])
        os.makedirs(path, exist_ok=True)
    elif f_index:
        make_file(command[-1])


if __name__ == "__main__":
    get_terminal_content()
