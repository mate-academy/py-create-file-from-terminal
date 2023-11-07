import os
import sys
from datetime import datetime
from typing import List


def parse_args(args: List[str]) -> dict:
    result = {}
    if args[1] == "-f":
        result["filename"] = args[2]
        result["dirs"] = args[4:]
    if args[1] == "-d":
        result["filename"] = args[-1]
        result["dirs"] = args[2:-2]
    return result


def write_content(path: str) -> None:
    line_number = 0
    with open(path, "w") as input_file:
        input_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        line_number += 1
        with open(path, "a") as input_file:
            input_file.write(f"{line_number} " + line + "\n")


def create_file(args: List[str]) -> None:
    if "-d" in args and "-f" not in args:
        path = os.path.join(*args[2:])
        os.makedirs(path, exist_ok=True)
        return
    if "-f" in args and "-d" not in args:
        path = args[2]
        write_content(path)
        return
    if "-f" in args and "-d" in args:
        filename = parse_args(args)["filename"]
        dirs = parse_args(args)["dirs"]
        path = os.path.join(*dirs, filename)
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        write_content(path)
        return


if __name__ == "__main__":
    create_file(sys.argv)
