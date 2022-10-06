import os
import sys
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    if "-f" not in command:
        path = os.path.join(*command[2:])

        if not os.path.exists(path):
            os.makedirs(path)

        return

    path = ""
    if "-d" in command:
        path = os.path.join(*command[2:-2])
        if not os.path.exists(path):
            os.makedirs(path)

    with open(f"{os.path.join(path, command[-1])}", "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break

            file.write(f"{line_num} {line}\n")
            line_num += 1


if __name__ == '__main__':
    create_file()