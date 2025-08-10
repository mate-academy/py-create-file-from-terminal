import sys
import os
from datetime import datetime


def create_file() -> None:
    if "-d" in sys.argv:
        new_path = []
        for command in sys.argv[sys.argv.index("-d") + 1:]:
            if command == "-f":
                break
            else:
                new_path.append(command)
        os.makedirs(os.path.join(*new_path), exist_ok=True)
        os.chdir(os.path.join(*new_path))

    if "-f" in sys.argv:
        with open(sys.argv[sys.argv.index("-f") + 1], "a") as new_file:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_file.write(current_datetime + "\n")
            line = 1
            while True:
                string = input("Enter content line: ")
                if string == "stop":
                    new_file.write("\n")
                    break
                new_file.write(f"{str(line)} {string}\n")
                line += 1


create_file()
