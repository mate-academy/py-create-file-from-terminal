import sys
import os
from _datetime import datetime


def parse_args(argv: list) -> dict:
    flags = {}
    i = 0
    while i < len(argv):
        if argv[i].startswith("-"):
            if i + 1 < len(argv) and not argv[i + 1].startswith("-"):
                flags[argv[i]] = argv[i + 1]
                i += 2
            else:
                flags[argv[i]] = True
                i += 1
        else:
            i += 1
    return flags


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


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
