import os
import argparse
from datetime import datetime
from argparse import Namespace


def put_content(file_name: str) -> None:
    with open(file_name, "a+") as file:
        file.write(create_content())


def create_content() -> str:
    content = []
    line = 0
    while True:
        string = input("Enter content line: ")
        if string == "stop":
            break
        line += 1
        content.append(str(line) + " " + string)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return timestamp + "\n" + "\n".join(content) + "\n\n"


def parser_func() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+",
                        help="Command to create directory")
    parser.add_argument("-f", "--filename",
                        help="Command to create file")
    return parser.parse_args()


def create_file_by_path() -> None:
    args = parser_func()

    if args.directory:
        directory = os.path.join(os.getcwd(), *args.directory)
        os.makedirs(directory)
    else:
        directory = os.getcwd()

    if args.filename:
        filename = (os.path.join(directory, args.filename))
        put_content(filename)


if __name__ == "__main__":
    create_file_by_path()
