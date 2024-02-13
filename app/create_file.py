import argparse
import os
from datetime import datetime


def validate_input(args: argparse.Namespace) -> None:
    if not args.directory and not args.file:
        raise argparse.ArgumentError(None,
                                     "At least one flag must be "
                                     "specified: -d/--directory or -f/--file.")
    if args.directory and not args.paths:
        raise argparse.ArgumentError(None,
                                     "The directory must be specified")


def create_directory(args: argparse.Namespace) -> None:
    path_to_directory = os.path.join(*args.paths)
    if not os.path.exists(path_to_directory):
        os.makedirs(path_to_directory)


def create_file(args: argparse.Namespace) -> None:
    if args.directory:
        create_directory(args)
        file_path = os.path.join(*args.paths, args.file)
    else:
        file_path = args.file
    with open(file_path, "a") as file:
        file.write((datetime.now()).strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                file.write("\n")
                break
            file.write(input_line + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Create a directory and a file.")
    parser.add_argument("-d", "--directory", action="store_true",
                        help="Create a directory.")
    parser.add_argument("-f", "--file", action="store",
                        help="Create a file.")
    parser.add_argument("paths", nargs="*",
                        help="Paths to create the file.")

    args = parser.parse_args()
    validate_input(args)

    if args.directory and args.file is None:
        create_directory(args)

    elif args.file:
        create_file(args)


if __name__ == '__main__':
    main()
