from datetime import datetime
from typing import LiteralString
import os
import sys


def file_content_printer(file_name: str) -> None:
    with open(file_name, "a") as file:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=file)
        counter = 1
        while True:
            line = input("Enter content line: ")
            if "stop" in line:
                break
            print(f"{counter} {line}", file=file)
            counter += 1


def create_path(argv: list) -> LiteralString | str | bytes:
    path = os.path.join(*filter(lambda x: "." not in x
                                          and x not in ["-f", "-d"], argv[1:]))
    return path


if "-d" in sys.argv and "-f" in sys.argv:
    path = create_path(sys.argv)
    file_name = filter(lambda x: "." in x, sys.argv[1:])
    os.makedirs(path)
    file_content_printer(f"{os.path.join(path, *file_name)}")
elif sys.argv[1] == "-d":
    os.makedirs(create_path(sys.argv))
elif sys.argv[1] == "-f":
    file_content_printer(sys.argv[2])
