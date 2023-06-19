import os
import argparse
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a+") as file:
        file.write(put_content())


def put_content() -> str:
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+",
                        help="Command to create directory")
    parser.add_argument("-f", "--filename",
                        help="Command to create file")
    args = parser.parse_args()

    if args.directory:
        directory = os.path.join(os.getcwd(), *args.directory)
        os.makedirs(directory)
    else:
        directory = os.getcwd()

    filename = (os.path.join(directory, args.filename)
                if args.filename else None)

    if filename:
        create_file(filename)
