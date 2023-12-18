import datetime

import os

import argparse


def create_file(directory: str | None, filename: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    full_path = os.path.join(directory, filename)

    if os.path.exists(full_path):
        with open(full_path, "a") as file:
            file.write(f"\n\n{timestamp}\n")
    else:
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(full_path, "w") as file:
            file.write(f"{timestamp}\n")

    with open(full_path, "a+") as file:
        string_num = 1

        while True:
            input_line = input("Enter content line: ")

            if input_line == "stop":
                return

            file.write(f"\n{string_num} {input_line}")
            string_num += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--filename")
    args = parser.parse_args()

    directory = os.path.join(*args.directory) if args.directory else ""
    filename = args.filename

    create_file(directory, filename)


if __name__ == "__main__":
    main()
