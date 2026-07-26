import sys
import os
from datetime import datetime
from typing import List


def parse_sys_args(sys_args: List[str]) -> dict:
    parsed_sys_args = {
        "commands": [],
        "path": [],
        "file_name": ""
    }

    for arg in sys_args[1:]:
        if arg.startswith("-"):
            parsed_sys_args["commands"].append(arg)
        elif "." in arg:
            parsed_sys_args["file_name"] += arg
        else:
            parsed_sys_args["path"].append(arg)

    return parsed_sys_args


def create_dirs(path: str) -> None:
    os.makedirs(path)


def create_file(current_time: datetime, path: str) -> None:
    with open(path, "a") as source_file:
        line_counter = 1
        source_file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                source_file.write(" \n")
                break
            source_file.write(f"{line_counter} {text}\n")
            line_counter += 1


def create_app() -> None:
    current_time = datetime.now()
    parsed_args = parse_sys_args(sys.argv)
    path = os.path.join("", *parsed_args["path"])
    path_file = os.path.join(
        "",
        *parsed_args["path"],
        parsed_args["file_name"]
    )

    if "-d" in parsed_args["commands"] and "-f" in parsed_args["commands"]:
        create_dirs(path)
        create_file(current_time, path_file)
        return
    if "-d" in parsed_args["commands"]:
        create_dirs(path)
    if "-f" in parsed_args["commands"]:
        create_file(
            current_time,
            path_file)


create_app()
