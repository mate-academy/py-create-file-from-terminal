import os
import argparse

from datetime import datetime


def create_directories(directories: list) -> str:
    path_to_file = os.path.join(*directories)
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)

    return path_to_file


def create_file(path: str, filename: str, lines: str) -> None:
    path = os.path.join(path + "/" + filename)
    with open(path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"{lines}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", type=str, nargs="+", help="Path to file")
    parser.add_argument("-f", type=str, help="Filename")
    args = parser.parse_args()

    path_to_file = os.getcwd()
    content = []

    if args.d is not None:
        path_to_file = create_directories(args.d)

    if args.f is not None:
        string_number = 1
        while True:
            string = input("Enter content line: ")
            if string == "stop":
                break
            content.append(f"{string_number} {string}")
            string_number += 1

        create_file(path_to_file, args.f, "\n".join(content))
