import sys
from datetime import datetime
import os


def create_file_cli(_: str, command: str, *args: list[str]) -> None:
    path = "app"
    if command == "-d":
        for item in args:
            if item == "-f":
                break
            path = os.path.join(path, item)
            os.makedirs(path)
    if args.count("-f"):
        with open(os.path.join(path, args[-1]), "w") as file:
            file.writelines(
                datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n"
            )
            while True:
                new_line = input("Enter content line: ")
                if new_line == "stop":
                    break
                file.writelines(new_line + "\n")


if __name__ == "__main__":
    create_file_cli(*sys.argv)
