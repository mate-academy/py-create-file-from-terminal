import os
from datetime import datetime
import argparse


def create_file(file_path):
    time_now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{time_now_str}\n")
        line_count = 1
        while True:
            line = input()
            if line.lower() == "stop":
                break
            file.write(f"{line_count} {line}\n")
            line_count += 1


def create_dir(directory_path):
    os.makedirs(directory_path, exist_ok=True)


def management_by_terminal():
    parser = argparse.ArgumentParser(description="Create directory or file with content.")
    parser.add_argument("-d", nargs="+", help="Create directories")
    parser.add_argument("-f", help="Create or update file")

    args = parser.parse_args()

    if args.d:
        create_dir(os.path.join(*args.d))

    if args.f:
        create_file(args.f)


if __name__ == "__main__":
    management_by_terminal()
