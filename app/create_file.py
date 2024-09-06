import argparse
import os
from datetime import datetime
from typing import Any


def parse_args() -> Any:
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", action="store")
    parser.add_argument("-d", action="store", nargs="*")

    return parser.parse_args()


def create_directories(directories: list) -> None:
    path = os.path.join(os.curdir, *directories)
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


def write_content_to_file(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
        file.write("\n")


args = parse_args()

if args.f is None and args.d is None:
    raise SystemExit("At least one argument must be specified")

if args.d is not None:
    create_directories(args.d)

if args.f is not None:
    write_content_to_file(args.f)