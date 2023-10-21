import argparse
import os
from datetime import datetime


def make_dir(dir_location: list) -> str:
    dir_location = os.path.join(*dir_location)
    os.makedirs(dir_location, exist_ok=True)
    return dir_location


def make_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Enter content or 'stop'")
        for counter, line in enumerate(iter(input, "stop")):
            print(f"{counter + 1} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()
    if args.d:
        new_working_directory = make_dir(args.d)
        os.chdir(new_working_directory)
    if args.f:
        make_file(args.f)


if __name__ == "__main__":
    main()
