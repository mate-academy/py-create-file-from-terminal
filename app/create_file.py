import argparse
import os
from datetime import datetime


def write_from_input(file_name: str) -> None:
    write_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    while True:
        text_input = input("Enter content line: ")
        if text_input == "stop":
            break
        write_text += text_input + "\n"
    print(write_text)
    with open(file_name, "a") as file:
        file.write(write_text)


def create_file() -> None:
    parser = argparse.ArgumentParser(description="Create file.")
    parser.add_argument("-d", "--directory", action="extend",
                        nargs="+", help="Directory path")
    parser.add_argument("-f", "--file", help="File name")
    args = parser.parse_args()

    if args.directory and args.file:

        file_path = "/".join(args.directory)

        os.makedirs(file_path, exist_ok=True)
        write_from_input(file_path + "/" + args.file)
        return None
    elif args.file:
        write_from_input(args.file)
    elif args.directory:
        file_path = "/".join(args.directory)
        os.makedirs(file_path, exist_ok=True)


create_file()
