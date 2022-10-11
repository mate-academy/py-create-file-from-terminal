import sys
import os
from datetime import datetime


def create_file() -> None:
    info = sys.argv
    path = ""

    if "-f" not in info:
        path = os.path.join(*info[2:])

        if not os.path.exists(path):
            os.makedirs(path)

    if "-d" in info:
        path += os.path.join(*info[2: -2])

        if os.path.exists(rf"{path}\{info[-1]}") is False:
            os.makedirs(path)

    with open(rf"{path}\{info[-1]}", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = ""
        line_two = 0
        while (line := input("Enter content line: ")) != "stop":
            lines += f"{line_two} {line}\n"
            line_two += 1

        if lines:
            file.write(f"{current_time}\n{lines}\n")


if __name__ == "__main__":
    create_file()
