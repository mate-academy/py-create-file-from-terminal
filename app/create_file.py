import os

from datetime import datetime

import argparse


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_dictionary(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path: str) -> None:
    with open(path, "a") as f:
        f.write(f'{datetime.now().strftime("%m-%d-%Y %H:%M:%S")}\n')
        new_content = input("Enter new line of content: ")

        number_string = 1
        while new_content != "stop":
            f.write(f"{number_string} {new_content}\n")
            new_content = input("Enter new line of content: ")
            number_string += 1


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, nargs="*")
parser.add_argument("-d", "--dir", type=str, nargs="*")
args = parser.parse_args()

if args.file and args.dir:
    create_dictionary(create_path(args.dir))
    create_file(os.path.join(create_path(args.dir), *args.file))

elif args.dir:
    create_dictionary(create_path(args.dir))

elif args.file:
    create_file(create_path(args.file))
