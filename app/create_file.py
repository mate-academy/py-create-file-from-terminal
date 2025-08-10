import os
import argparse
import datetime
from argparse import Namespace


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", help="directory path")
    parser.add_argument("-f", help="file name")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    file_path = args.f

    if args.d:
        dir_path = os.path.join(*args.d)
        os.makedirs(dir_path, exist_ok=True)

    if file_path:
        if args.d:
            file_path = os.path.join(dir_path, file_path)

        existing = os.path.exists(os.path.abspath(file_path))
        if existing is True:
            open_mode = "a"
            line_break = "\n"
        else:
            open_mode = "w"
            line_break = ""

        with open(file_path, open_mode) as file:
            file.write(datetime.datetime.now().strftime(
                line_break + "%Y-%m-%d %H:%M:%S" + "\n"))
            counter = 0
            while (line := input("Enter content line:")) != "stop":
                counter += 1
                file.write(f"{counter} " + line + "\n")


if __name__ == "__main__":
    main()
