import sys
import os
from datetime import datetime
from typing import List, Dict, Any


def parse_arguments(arguments: List[str]) -> Dict[str, Any]:
    flags = {"-d": [], "-f": ""}
    current_flag = None

    for arg in arguments:
        if arg in flags:
            current_flag = arg
        elif current_flag == "-d":
            flags[current_flag].append(arg)
        elif current_flag == "-f":
            flags[current_flag] = arg
    return flags


def create_directories(directory_names: List[str]) -> None:
    for name in directory_names:
        if name:
            os.makedirs(name, exist_ok=True)


def create_file(
        directory_path: str,
        file_name: str,
        content_lines: List[str]
) -> None:
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        full_path = (
            os.path.join(directory_path, file_name)
            if directory_path else file_name
        )
        with open(full_path, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for i, line in enumerate(content_lines, start=1):
                file.write(f"{i} {line}\n")


def main() -> None:
    flags = parse_arguments(sys.argv[1:])
    directory_names = flags["-d"]
    file_name = flags["-f"]
    content_lines = []

    if file_name:
        print("Enter line of content:")
        while True:
            content_line = input()
            if content_line.lower() == "stop":
                break
            content_lines.append(content_line)

    if directory_names:
        for directory_name in directory_names:
            directory_path = os.path.join(os.getcwd(), directory_name)
            os.makedirs(directory_path, exist_ok=True)
            create_file(directory_path, file_name, content_lines)
    elif file_name:
        create_file("", file_name, content_lines)
