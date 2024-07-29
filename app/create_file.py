import os.path
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    directory = ""

    if args[0] == "-d":
        directory = args[1:]
        if "-f" in args:
            directory = directory[:args.index("-f") - 1]
            args = args[args.index("-f"):]

        try:
            os.makedirs("/".join(directory))
        except FileExistsError:
            print("Directory already exist")

    if args[0] == "-f":
        try:
            _make_file(directory, args[1])
        except FileNotFoundError:
            print("File not found")


def _make_file(directory: list[str], filename: str) -> None:
    mode = "w"
    if os.path.exists(filename):
        mode = "a"
    with open(os.path.join(*directory, filename), mode) as file:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_date + "\n")

        count = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{count} {content}\n")
            count += 1
        file.write("\n")
