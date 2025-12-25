import argparse
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d%H:%M:%S")

    with open(file_path, "a") as file:
        file.write(current_time + "\n")

    with open(file_path, "a") as file:
        line_num = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            file.write(f"{line_num} {line}" + "\n")
            line_num += 1


def interaction_func() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--filename", nargs="?")
    args = parser.parse_args()

    if not args.filename:
        os.makedirs("/".join(args.directory), exist_ok=True)
    if not args.directory:
        create_file(args.filename)
    else:
        os.makedirs("/".join(args.directory), exist_ok=True)
        full_path = os.path.join("/".join(args.directory), args.filename)
        create_file(str(full_path))


if __name__ == "__main__":
    interaction_func()
