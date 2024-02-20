import argparse
from datetime import datetime
import os


def create_file_from_input(dir_path: str, file_name: str) -> None:
    with open(os.path.join(dir_path, file_name), "w") as file:
        content_lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        input_line = ""

        while input_line.lower() != "stop":
            input_line = input("Enter content line:")

            if input_line != "stop":
                content_lines.append(input_line)

        file.write("\n".join(content_lines))


def create_file() -> None:
    parser = argparse.ArgumentParser(description="File creating arguments")

    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        help="directory names"
    )
    parser.add_argument("-f", "--filename", help="file name")

    args = parser.parse_args()

    dir_path = os.path.join(*args.directories if args.directories else "")

    if args.directories:
        os.makedirs(dir_path, exist_ok=True)

    if args.filename:
        create_file_from_input(dir_path, args.filename)


create_file()
