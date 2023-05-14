from argparse import ArgumentParser
from datetime import datetime
import os


def create_directory(directory: list[str]) -> None:
    new_path = os.path.join(*directory)
    os.makedirs(new_path)


def create_file(name_file: str) -> None:
    with open(name_file, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count_of_line = 1
        while True:
            new_line = input("Enter content line: ") + "\n"
            file.write(f"{count_of_line} {new_line}")
            count_of_line += 1
            if "stop" in new_line:
                file.write("\n")
                break


def create_file_in_new_directory() -> None:
    parser = ArgumentParser()
    commands = parser.add_argument_group()
    commands.add_argument("-d", "--directory", nargs="+")
    commands.add_argument("-f", "--file")
    args = parser.parse_args()
    if args.directory and args.file:
        new_path_with_file = os.path.join(*args.directory, args.file)
        create_directory(args.directory)
        create_file(new_path_with_file)
    elif args.directory:
        create_directory(args.directory)
    elif args.file:
        create_file(args.file)


if __name__ == "__main__":
    create_file_in_new_directory()
