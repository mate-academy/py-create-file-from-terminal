import os
import sys
from datetime import datetime
from typing import List


def parse_args(arguments: List[str]) -> dict:
    parsed_args = {"file": None, "directory": []}
    flag = None

    for argument in arguments:
        if argument in ["-f", "-d"]:
            flag = argument
        elif flag == "-f":
            parsed_args["file"] = argument
        elif flag == "-d":
            parsed_args["directory"].append(argument)

    return parsed_args


def generate_file_path(parsed_arguments: dict) -> str:
    directory_path = ""
    if parsed_arguments["directory"]:
        directory_path = os.path.join(*parsed_arguments["directory"])
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    file_path = os.path.join(directory_path, parsed_arguments["file"])

    return file_path


def main() -> None:
    command_line_args = sys.argv[1:]
    parsed_args = parse_args(command_line_args)

    file_path = generate_file_path(parsed_args)

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a+") as file:
        file.write(formatted_datetime)
        file.write("\n")

        input_line = input("Enter content line: ")
        line_number = 1

        while input_line.lower() != "stop":
            file.write(f"{line_number} {input_line}\n")
            line_number += 1
            input_line = input("Enter content line: ")

        file.write("\n")


if __name__ == "__main__":
    main()
