import sys
import os
from _datetime import datetime


def parse_args(argv: list) -> dict:
    flags = {}
    for i, arg in enumerate(argv):
        if arg.startswith("-") and i + 1 < len(argv):
            flags[arg] = argv[i + 1]
    return flags


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")


def write_to_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower().strip() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    flags = parse_args(sys.argv)

    if "-d" in flags:
        create_directory(flags["-d"])

    if "-f" in flags:
        file_path = flags["-f"]
        if "-d" in flags:
            file_path = os.path.join(flags["-d"], flags["-f"])
        write_to_file(file_path)
