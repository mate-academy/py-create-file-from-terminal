import argparse
import os
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    line_number = 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as file:
        file.write(f"{timestamp}\n")
        while True:
            input_line = input("Enter content line: ")
            if input_line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {input_line}\n")
            line_number += 1


def create_file_from_terminal() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="path", nargs="+", help="directory path")
    parser.add_argument("-f", dest="name", help="file name")
    args = parser.parse_args()

    if args.path:
        dir_path = create_path(args.path)
        if args.name:
            file_path = os.path.join(dir_path, args.name)
            create_file(file_path)
    elif args.name:
        create_file(args.name)
    else:
        print("Error: Enter -d or -f flag.")


if __name__ == "__main__":
    create_file_from_terminal()
