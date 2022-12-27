from datetime import datetime
import os
import sys


def create_file() -> None:
    if "-d" in sys.argv:
        index = 2

        while len(sys.argv) != index:
            if sys.argv[index] == "-f":
                index += 1
                continue

            os.mkdir(sys.argv[index])
            os.chdir(sys.argv[index])
            index += 1

    if "-f" in sys.argv:
        with open(sys.argv[-1], "w") as f:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{date}\n")

            current_line = 1
            inline_content = input("Enter content line: ")

            while inline_content != "stop":
                f.write(f"Line{current_line} {inline_content}\n")
                inline_content = input("Enter content line: ")
                current_line += 1


create_file()
