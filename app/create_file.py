import sys

# import os
from pathlib import Path


def validation(arguments: list) -> None:
    if "-f" not in arguments:
        raise ValueError("-f parameter expected")
    if arguments[-1] == "-f":
        raise ValueError("Name of file expected")
    if arguments.count("-f") > 1:
        raise ValueError("So many -f arguments")

    if arguments[1] not in ["-f", "-d"]:
        raise ValueError("first parameter should be -f or -d")

    if "-d" in arguments:
        if arguments[1] != "-d":
            raise ValueError("expected argument -d out of range")
        if arguments[2] == "-f":
            raise ValueError("Expected directory name after -d")
        if arguments.count("-d") > 1:
            raise ValueError("So many -d arguments")


def create_folders(arguments: list) -> None:
    print("Llega")
    path = Path()
    for i in range(arguments.index("-d") + 1, arguments.index("-f")):
        path = path / arguments[i]
        path.mkdir(exist_ok=True)


def main() -> None:
    validation(sys.argv)
    arguments = sys.argv
    if "-d" in arguments:
        create_folders(arguments)


if __name__ == "__main__":
    main()
