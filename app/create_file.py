import os
from datetime import datetime
from argparse import ArgumentParser, Namespace


def make_path(file_path: str) -> str:
    curr_dir = os.getcwd()
    directories = os.path.normpath(file_path)

    curr_path = os.path.join(curr_dir, directories)

    if not os.path.exists(curr_path):
        os.makedirs(curr_path)

    return curr_path


def write_file(file_path: str) -> None:
    file_path = os.path.join(file_path, args.file)

    with open(file_path, "w") as destination:
        destination.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while (line := input("Enter content line:")) != "stop":
            destination.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-d",
                        "--dir",
                        type=str,
                        help="creates directory inside current directory")

    parser.add_argument("-f",
                        "--file",
                        type=str,
                        help="creates file inside current directory")

    args: Namespace = parser.parse_args()

    path = ""

    if args.dir:
        path = make_path(args.dir)
    if args.file:
        write_file(path)
