import argparse
import os
from datetime import datetime


def create_dir(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


def collect_input() -> list:
    data = []
    count_number = 1
    while True:
        user_input = input('Write your string (or "stop" to end): ')
        if user_input.lower() == "stop":
            break
        data.append(f"{count_number} {user_input}")
        count_number += 1
    return data


def write_data_to_file(file_path: str, data: list) -> None:
    formatted_datetime = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(formatted_datetime + "\n")
        for line in data:
            file.write(line + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and file.")
    parser.add_argument("-d", "--directory",
                        nargs="*", help="Directory path to create")
    parser.add_argument("-f", "--file",
                        help="File to create")

    args = parser.parse_args()

    if args.directory:
        create_dir(args.directory)

    if args.file:
        file_path = os.path.join(
            *args.directory, args.file) if args.directory else args.file
        user_data = collect_input()
        write_data_to_file(file_path, user_data)


if __name__ == "__main__":
    main()
