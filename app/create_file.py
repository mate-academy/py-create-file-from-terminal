import sys
from datetime import datetime
import os


def create_file_cli(_: str, *args: list[str]) -> None:
    path = os.path.join("app")
    if args[0] == "-d":
        for i in range(1, len(args)):
            if args[i] == "-f":
                break
            path = os.path.join(path, args[i])
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
