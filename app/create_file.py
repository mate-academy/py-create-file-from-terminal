from datetime import datetime
import sys
import os
from contextlib import contextmanager
from typing import Any


@contextmanager
def get_file(name: str) -> Any:
    path = os.path.join(os.getcwd(), name)
    if not os.path.exists(path):
        file = open(path, "w")
    else:
        file = open(path, "a")
    file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
    yield file
    file.close()


def write_to_file(name: str) -> None:
    with get_file(name) as f:
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{counter} {content}\n")
            counter += 1


def create_dirs(names: list[str]) -> None:
    if len(names) == 1:
        os.mkdir(names[0])
    else:
        os.makedirs(os.path.join(*names), exist_ok=True)


if __name__ == "__main__":
    args = sys.argv
    print(args)
    if args[1] not in ["-f", "-d"]:
        raise ValueError("Wrong flags")
    if sum(value in ["-f", "-d"] for value in args) == 2:
        f_index = args.index("-f")
        create_dirs(args[2:f_index])
        write_to_file(os.path.join(*args[2:f_index], args[-1]))
    elif args[1] == "-f":
        if not args[2] or len(args[2].split(".")) != 2:
            raise ValueError("Needed file name")
        write_to_file(args[2])
    elif args[1] == "-d":
        if not args[2:]:
            raise ValueError("Needed dir names")
        create_dirs(args[2:])
