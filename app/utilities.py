import os
import sys
from datetime import datetime
from exceptions import WrongNumberOfArguments, ArgumentsCantBeParsed


def parse_command_line_args() -> dict:
    parsed_args = {
        "-d": None,
        "-f": None
    }

    if not (3 <= len(sys.argv) <= 6):
        raise WrongNumberOfArguments(len(sys.argv))

    if len(sys.argv) == 3 and "-f" in sys.argv:
        parsed_args["-f"] = sys.argv[2]
        return parsed_args
    if len(sys.argv) == 4 and "-d" in sys.argv:
        parsed_args["-d"] = [sys.argv[2], sys.argv[3]]
        return parsed_args
    if len(sys.argv) == 6 and "-f" in sys.argv and "-d" in sys.argv:
        parsed_args["-d"] = [sys.argv[2], sys.argv[3]]
        parsed_args["-f"] = sys.argv[5]
        return parsed_args

    raise ArgumentsCantBeParsed(f"Given arguments {sys.argv[1:]} "
                                f"can not be parsed")


def create_directories(parsed_args: dict) -> None:
    os.makedirs(os.path.join(*parsed_args["-d"]))


def create_file(parsed_args: dict) -> None:
    file_path = parsed_args["-f"]
    if parsed_args["-d"]:
        file_path = (f"{parsed_args["-d"][0]}"
                     f"/{parsed_args["-d"][1]}"
                     f"/{parsed_args["-f"]}")

    content_lines = []

    line = ""
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    with open(file_path, "w") as file:
        file.write(
            f"{datetime.strftime(datetime.now(),
                                 '%Y-%m-%d %I:%M:%S')}"
            f"\n"
        )

        for index, line in enumerate(content_lines):
            file.write(f"{index + 1} {line} \n")
