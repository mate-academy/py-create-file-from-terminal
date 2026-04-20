import os
import argparse
from datetime import datetime


def input_from_terminal() -> str:
    count = 1
    content = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        content += f"{str(count)} {text} \n"
        count += 1

    return content


def create_file(path_to_file: str, file_name: str) -> None:
    if path_to_file:
        os.makedirs(path_to_file, exist_ok=True)
    with open(os.path.join(path_to_file, file_name), "a") as file_obj:
        file_obj.write(input_from_terminal())


def parse_input() -> None:
    parser = argparse.ArgumentParser(description="My program")
    parser.add_argument("-d", nargs="+", help="part of the path")
    parser.add_argument("-f", help="file name")
    args = parser.parse_args()

    file_name = args.f

    if args.d and args.f:
        create_file(os.path.join(*args.d), file_name)
    elif args.d:
        os.makedirs(os.path.join(*args.d), exist_ok=True)
    elif args.f:
        create_file("", file_name)


if __name__ == "__main__":
    parse_input()
