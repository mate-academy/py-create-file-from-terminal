import os
from argparse import Namespace
from datetime import datetime

from parser import create_parser


def create_dirs(arguments: Namespace) -> str:
    new_path = os.path.join(*arguments.dir)
    os.makedirs(new_path, exist_ok=True)
    return new_path


def create_file(path: str, arguments: Namespace) -> None:
    with open(os.path.join(path, arguments.file[0]), "a") as file:
        file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S\n"))
        line_num = 1
        line_in = input("Enter content line: ")
        while line_in != "stop":
            file.write(f"{line_num} {line_in}\n")
            line_in = input("Enter content line: ")
            line_num += 1
        file.write("\n")


def main() -> None:
    path = ""
    args = create_parser().parse_args()

    if args.dir:
        path = create_dirs(args)

    if args.file:
        create_file(path, args)
