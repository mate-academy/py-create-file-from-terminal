import argparse

import datetime

import os

parser = argparse.ArgumentParser()

parser.add_argument("-d", nargs="+")

parser.add_argument("-f")

args = parser.parse_args()


def create_path(path: list[str]) -> str:
    path = os.path.join(*path)
    return path


def make_dirs(dirs_path: str) -> None:
    os.makedirs(dirs_path, exist_ok=True)


def create_and_write_in_file(file_path: str) -> None:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
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

        path_to_create_file = [*args.d, args.f]

        create_and_write_in_file(create_path(path_to_create_file))

        return

    if args.d:
        dears_to_create = create_path(args.d)
        make_dirs(dears_to_create)

    if args.f:
        file_name = args.f
        create_and_write_in_file(os.path.abspath(file_name))


if __name__ == "__main__":
    create_file()
