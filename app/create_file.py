import argparse
import os
from datetime import datetime


def file_contents(file_name: str) -> None:
    text_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    while True:
        text_input = input("Enter content line: ")
        if text_input == "stop":
            break
        text_content += text_input + "\n"
        print(text_content)
        with open(file_name, "a") as file:
            file.write(text_content)


def create_file() -> None:
    parser = argparse.ArgumentParser(description="Create file from terminal")
    parser.add_argument("-d", "--directory", action="extend",
                        nargs="+", help="Directory path to create")
    parser.add_argument("-f", "--file", help="File's name")
    args = parser.parse_args()

    if args.directory and args.file:
        file_path = "/".join(args.directory)
        os.makedirs(file_path, exist_ok=True)
        file_contents(file_path + "/" + args.file)
        return
    elif args.file:
        file_contents(args.file)
    elif args.directory:
        file_path = "/".join(args.directory)
        os.makedirs(file_path, exist_ok=True)


create_file()

