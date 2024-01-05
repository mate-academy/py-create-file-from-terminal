import argparse
import os
from datetime import datetime


def append_file_line(full_path_plus_filename: str) -> None:
    count = 1
    file_exists = os.path.exists(full_path_plus_filename)
    with open(full_path_plus_filename, "a") as file:
        if file_exists:
            file.write(f"\n")
        formatted_datetime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{formatted_datetime}\n")
        another_line = ""
        if file_exists:
            another_line = "Another "
        while True:
            line_annotation = f"{count} Line{count}"
            if file_exists:
                line_annotation = f"{count} Another line{count}"
            input_line = input(f"Enter content line: {another_line}")
            if input_line == "stop":
                break
            file.write(f"{line_annotation} {input_line}\n")
            count += 1


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        nargs="*",
        action="store",
        dest="file_directory"
    )
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        dest="file_name"
    )
    args = parser.parse_args()

    full_path = ""
    if args.file_directory:
        full_path = os.path.join(*args.file_directory)
        os.makedirs(full_path, exist_ok=True)
    if args.file_name:
        full_path_plus_filename = os.path.join(full_path, args.file_name)
        append_file_line(full_path_plus_filename)


if __name__ == "__main__":
    create_file()
