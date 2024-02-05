import os
from datetime import datetime
import argparse


def create_file(file_path: str) -> None:
    time_now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{time_now_str}\n")
        line_count = 1
        while True:
            line = input("Enter content line:")
            if line.lower() == "stop":
                break
            file.write(f"{line_count} {line}\n")
            line_count += 1


def create_dir(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def create_dir_and_file(directory_path: str, file_name: str) -> None:
    create_file(directory_path)
    file_path = os.path.join(directory_path, file_name)
    create_file(file_path)


def management_by_terminal() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content."
    )
    parser.add_argument("-d", nargs="+", help="Create directories")
    parser.add_argument("-f", help="Create or update file")

    args = parser.parse_args()

    if args.d:
        for directory in args.d:
            create_dir(directory)
    elif args.f:
        create_file(args.f)
    elif args.d and args.f:
        for directory in args.d:
            create_dir_and_file(directory, args.f)


if __name__ == "__main__":
    management_by_terminal()
