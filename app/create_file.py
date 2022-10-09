import sys
import os
from datetime import datetime


def create_file() -> None:
    if "-d" in sys.argv:

        index = 2

        while len(sys.argv) != index and sys.argv[index] != "-f":
            os.mkdir(sys.argv[index])
            os.chdir(sys.argv[index])
            index += 1

    if "-f" in sys.argv:
        with open(sys.argv[-1], "w") as file:
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
