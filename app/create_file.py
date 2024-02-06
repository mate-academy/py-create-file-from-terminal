import argparse

import datetime

import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+")

parser.add_argument("-f", nargs="+")

args = parser.parse_args()


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def make_dirs(way: str) -> None:
    os.makedirs(way, exist_ok=True)


def create_and_write_in_file(file_name: str) -> None:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{formatted_datetime}\n")
        number_of_line = 1

        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break

            file.write(f"{number_of_line} {text}\n")
            number_of_line += 1

        file.write("\n")


def create_file() -> None:
    if args.d and args.f:
        make_dirs(create_path(args.d))

        path_to_create_file = args.d + args.f

        create_and_write_in_file(create_path(path_to_create_file))

        return None

    if args.d:
        dears_to_create = create_path(args.d)
        make_dirs(dears_to_create)

    if args.f:
        file_name = args.f[0]
        create_and_write_in_file(os.path.abspath(file_name))


if __name__ == "__main__":
    create_file()
