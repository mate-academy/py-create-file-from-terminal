import os
import argparse
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", type=str, nargs="+", default=[])
    parser.add_argument("-f", type=str, default="")
    args = parser.parse_args()

    directory = args.d
    filename = args.f
    full_path = os.path.join("/".join(directory), filename)

    if directory:
        os.makedirs("/".join(directory), exist_ok=True)

    if filename:
        with open(os.path.join(full_path), "a") as file:
            now = datetime.now()
            file.write(f"{now.strftime('%m/%d/%Y, %H:%M:%S')}\n")

            new_line = input("Enter a new line or 'stop' to exit: ")

            line_count = 1

            while new_line != "stop":
                file.write(f"{line_count} {new_line}\n")
                line_count += 1
                new_line = input("Enter a new line or 'stop' to exit: ")


if __name__ == '__main__':
    create_file()
