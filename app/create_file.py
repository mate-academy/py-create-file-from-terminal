import os
import sys
from typing import Any
from datetime import datetime
from collections import namedtuple


def file_content_printer(current_file: str) -> None:
    with open(current_file, "a") as new_file:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=new_file)
        counter = 1
        while True:
            line = input("Enter content line: ")
            if "stop" in line:
                break
            print(f"{counter} {line}", file=new_file)
            counter += 1


def create_path(argv: list) -> Any | str:
    PathVariants = namedtuple("PathVariants", ["path", "path_with_fn"])
    try:
        path = os.path.join(*filter(
            lambda x: "." not in x and x not in ("-f", "-d"), argv[1:])
        )
        path_with_fn = os.path.join(
            path,
            *filter(lambda x: "." in x, sys.argv[1:])
        )
        return PathVariants(path, path_with_fn)
    except TypeError:
        f_name = list(filter(lambda x: "." in x, sys.argv[1:]))[0]
        return PathVariants(None, f_name)


if os.path.exists(create_path(sys.argv).path_with_fn):
    file_content_printer(create_path(sys.argv).path_with_fn)
elif "-d" in sys.argv and "-f" in sys.argv:
    file_name = filter(lambda x: "." in x, sys.argv[1:])
    os.makedirs(create_path(sys.argv).path, exist_ok=True)
    file_content_printer(create_path(sys.argv).path_with_fn)
elif sys.argv[1] == "-d":
    os.makedirs(create_path(sys.argv).path)
elif sys.argv[1] == "-f":
    file_content_printer(sys.argv[2])
