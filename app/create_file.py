import sys
import os
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    path = ""

    if "-d" in command:
        path = os.path.join(*command[2: -2])
        os.makedirs(path)

    if "-f" in command:
        with open(command[-1], "w") as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date}\n")
            line = 1
            content = input("Enter content line: ")
            while content != "stop":
                file.write(f"Line{line} {content}")
                content = input("Enter content line: ")
                line += 1


if __name__ == "__main__":
    create_file()
