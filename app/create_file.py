import argparse
import os
from datetime import datetime


def add_content(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(timestamp + "\n")
        line_index = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                file.write(" \n")
                break
            file.write(f"{line_index} {content}\n")
            line_index += 1


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dirs", nargs="*")
    parser.add_argument("-f", dest="file")
    args = parser.parse_args()
    file_path = os.getcwd()

    if args.dirs:
        file_path = os.path.join(file_path, *args.dirs)
        os.makedirs(file_path, exist_ok=True)

    if args.file:
        new_path = os.path.join(file_path, args.file)
        add_content(new_path)


if __name__ == "__main__":
    create_file()
