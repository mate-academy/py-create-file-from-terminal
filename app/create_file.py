import argparse
from datetime import datetime
from sys import argv
from os import path, makedirs
from typing import List


def argv_parser() -> type:
    parser = argparse.ArgumentParser(
        description="Create file in specified directory"
    )
    parser.add_argument("module_name", help="module name")
    parser.add_argument("-d", "--directory", nargs="*", default=[])
    parser.add_argument("-f", "--filename", default=None)
    return parser.parse_args(argv)


def command_reader() -> str:
    file_name = "file.txt"
    dir_path = None

    command_args = argv_parser()

    if command_args.directory:
        dir_path = path.join(*command_args.directory)

    if command_args.filename:
        file_name = command_args.filename

    if dir_path:
        file_name = path.join(dir_path, file_name)
        makedirs(dir_path, exist_ok=True)

    return file_name


def io_handker(file_exist: bool) -> list:
    output_data = []
    comment = "Line"

    if file_exist:
        comment = "Another line"
    else:
        output_data.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    line_number = 0

    while True:
        line_number += 1
        line = input(f"Enter content line: {comment}{line_number} ")
        if line == "stop":
            break
        output_data.append(f"{comment}{line_number}  {line}\n")

    return output_data


def file_handler(file_name: str, data: List[str]) -> None:

    with open(file_name, "a") as file_out:
        file_out.writelines(data)


def main() -> None:
    file_from_terminal = command_reader()
    data = io_handker(path.exists(file_from_terminal))
    file_handler(file_from_terminal, data)


if __name__ == "__main__":
    main()
