import os
import sys

from datetime import datetime
from typing import Any


data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def make_directory(name_dir: str | bytes) -> Any:
    os.makedirs(name_dir, exist_ok=True)
    return name_dir


def create_file(file_name: str) -> Any:
    with open(file_name, "a") as new_file:
        line_number = 1
        new_file.write(f"{data}\n")
        while True:
            new_line = input("Enter content line:")
            new_file.write(f"{line_number} {new_line} \n")
            line_number += 1
            if new_line.lower() == "stop":
                break

        new_file.write("\n")


def main() -> None:
    command = sys.argv[1:]

    f_ind = command.index("-f") if "-f" in command else None
    d_ind = command.index("-d") if "-d" in command else None

    if d_ind is not None and f_ind is None:
        make_directory(os.path.join(*command[d_ind + 1:]))
        return

    if f_ind is not None and d_ind is None:
        create_file(command[f_ind + 1])
        return

    if d_ind is not None and f_ind is not None:
        if d_ind < f_ind:
            file_dir = make_directory(os.path.join(*command[d_ind + 1:f_ind]))
            file_path = os.path.join(file_dir, command[f_ind + 1])
        else:
            file_dir = make_directory(os.path.join(*command[d_ind + 1:]))
            file_path = os.path.join(file_dir, command[f_ind + 1])

        create_file(file_path)

if __name__ == "__main__":
    main()
