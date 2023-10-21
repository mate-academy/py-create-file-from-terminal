import argparse
import os
from datetime import datetime


def make_dir(dir_locations: list) -> str:
    dir_location = os.path.join(*dir_locations)
    os.makedirs(dir_location, exist_ok=True)
    return dir_location


def make_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Enter content or 'stop'")
        for counter, line in enumerate(iter(input, 'stop'), 1):
            file.write(f"{counter} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs='+', help="List of directory names")
    parser.add_argument("-f", help="File name")
    args = parser.parse_args()

    if args.d:
        new_working_directory = make_dir(args.d)
        os.chdir(new_working_directory)

    if args.f:
        make_file(args.f)


if __name__ == '__main__':
    main()
