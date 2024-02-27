import os
import sys
from datetime import datetime
from typing import List


def parse_args(arguments: List[str]) -> dict:
    args = {"file": "", "directory": [], "flag": []}
    flag = None
    for argument in arguments:
        if argument in ["-d", "-f"]:
            flag = argument
            args["flag"].append(argument)
        elif flag == "-f":
            args["file"] = argument
        elif flag == "-d":
            args["directory"].append(argument)

    return args


def generate_file_path(parsed_arguments: dict) -> str:
    path_to_file = ""
    if "-d" in parsed_arguments["flag"] and "-f" in parsed_arguments["flag"]:
        path_to_file = os.path.join(
            *parsed_arguments["directory"], parsed_arguments["file"]
        )
        dir_path = os.path.dirname(path_to_file)
        os.makedirs(dir_path, exist_ok=True)

    elif "-d" in parsed_arguments["flag"]:
        path_to_file = os.path.join(*parsed_arguments["directory"])
        os.makedirs(path_to_file, exist_ok=True)

    elif "-f" in parsed_arguments["flag"]:
        path_to_file = parsed_arguments["file"]
        with open(path_to_file, "w"):
            pass

    return path_to_file


def write_line(path: str) -> None:

    formatted_datetime = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(path, "a") as file:
        file.write(formatted_datetime)
        file.write("\n")
        input_line = input("Enter content line: ")
        line_number = 0

        while input_line.lower() != "stop":
            line_number += 1
            file.write(f"{line_number} {input_line}\n")
            input_line = input("Enter content line: ")
        file.write("\n")


if __name__ == "__main__":
    command_line_args = sys.argv[1:]
    parsed_args = parse_args(command_line_args)
    file_path = generate_file_path(parsed_args)

    if ".txt" in file_path:
        write_line(file_path)
