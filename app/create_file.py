import os
import sys
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    args = sys.argv
    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        if d_index < f_index:
            path = os.path.join(*args[d_index + 1: f_index])
        else:
            path = os.path.join(*args[d_index + 1:])

        os.makedirs(path, exist_ok=True)
        create_file(os.path.join(path, file_name))

    elif "-d" in args:
        d_index = args.index("-d")
        path = os.path.join(*args[d_index + 1:])
        os.makedirs(path, exist_ok=True)

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)
