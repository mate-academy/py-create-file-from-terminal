from datetime import datetime
import sys
import os
from contextlib import contextmanager
from typing import Iterator, TextIO
from argparse import ArgumentParser


@contextmanager
def get_file(name: str) -> Iterator[TextIO]:
    source_file = open(name, "a")
    source_file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
    yield source_file
    source_file.close()


def write_to_file(name: str) -> None:
    with get_file(name) as source_file:
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{counter} {content}\n")
            counter += 1


def create_dirs(names: list[str]) -> None:
    if len(names) == 1:
        os.mkdir(names[0])
    os.makedirs(os.path.join(*names), exist_ok=True)


def create_dirs_and_file(filename: str, dirs: list[str]) -> None:
    create_dirs(dirs)
    write_to_file(os.path.join(*dirs, filename))


def init_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("-d", action="extend", nargs="+", type=str)
    parser.add_argument("-f", action="store", nargs=1, type=str)
    return parser


if __name__ == "__main__":
    parser = init_parser()
    namespace = parser.parse_args(sys.argv[1:])
    filename = getattr(namespace, "f", None)
    dirs = getattr(namespace, "d", None)
    if filename and dirs:
        create_dirs_and_file(filename[0], dirs)
    elif filename:
        write_to_file(filename[0])
    elif dirs:
        create_dirs(dirs)
