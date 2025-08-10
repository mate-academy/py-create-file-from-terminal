from __future__ import annotations
import os
import datetime
import argparse


def create_path() -> str | bytes | None:
    parser = argparse.ArgumentParser(description="Create a file")
    parser.add_argument(
        "-d", "--directories", nargs="+", help="List of directory names"
    )
    parser.add_argument("-f", "--file_name", help="Name of the file to create")

    args = parser.parse_args()

    directories = args.directories
    file_name = args.file_name

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(
            *directories, file_name
        ) if directories else file_name

        return file_path


def write_to_file() -> None:
    file_path = create_path()
    if file_path:
        with open(file_path, "a") as file_to_create:
            current_timestamp = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            if os.path.getsize(file_path) > 0:
                file_to_create.write("\n")

            file_to_create.write(current_timestamp + "\n")

            line_number = 0
            while True:
                file_content = input("Enter content line: ")
                line_number += 1
                if file_content == "stop":
                    break

                file_to_create.write(f"{line_number} {file_content}\n")
