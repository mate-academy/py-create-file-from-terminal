import os
import sys
from datetime import datetime
from typing import Any


def create_file() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        dir_args = args[args.index("-d") + 1:]
        dir_path = os.path.join(*dir_args)
        os.makedirs(dir_path)

        if "-f" in args:
            file_name = args[args.index("-f") + 1]
            file_path = os.path.join(dir_path, file_name)
            if os.path.exists(file_path):
                with open(file_path, "a") as file:
                    write_content(file)
            else:
                with open(file_path, "w") as file:
                    write_content(file)
    elif "-f" in args:
        file_name = args[args.index("-f") + 1]
        if os.path.exists(file_name):
            with open(file_name, "a") as file:
                write_content(file)
        else:
            with open(file_name, "w") as file:
                write_content(file)


def write_content(file_name: Any) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name.write(now + "\n")
    line_num = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_name.write(f"{line_num} {line}\n")
        line_num += 1


if __name__ == "__main__":
    create_file()
