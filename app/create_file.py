import sys
import os
from os import PathLike
from datetime import datetime


def parse_arguments() -> dict:
    parsed_args = {
        "file_name": "",
        "path": ""
    }
    arguments = sys.argv
    f_flag_index = None
    d_flag_index = None

    if "-f" in arguments:
        f_flag_index = arguments.index("-f")
        parsed_args["file_name"] = arguments[f_flag_index + 1]

    if "-d" in arguments:
        d_flag_index = arguments.index("-d")
        if not f_flag_index or d_flag_index > f_flag_index + 1:
            parsed_args["path"] = os.path.join(
                *arguments[d_flag_index + 1:]
            )
        else:
            parsed_args["path"] = os.path.join(
                *arguments[d_flag_index + 1:f_flag_index]
            )
    return parsed_args


def create_file(
    file_name: str,
    path: str | PathLike
) -> None:
    current_dir = os.getcwd()

    if path:
        os.makedirs(path, exist_ok=True)
        current_dir = path

    if file_name:
        file_path = os.path.join(current_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, "a+") as file:
                file.write("\n")

        with open(file_path, "a+") as file:
            creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{creation_date}\n")
            line_number = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1


def main() -> None:
    params = parse_arguments()
    create_file(params["file_name"], params["path"])


if __name__ == "__main__":
    main()
