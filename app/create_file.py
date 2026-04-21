import os
import sys
from datetime import datetime
from typing import List, Tuple


def parse_arguments(arguments: List[str]) -> Tuple[List[str], str]:
    directory_parts: List[str] = []
    file_name: str = ""
    current_mode: str = ""

    for argument in arguments:
        if argument == "-d":
            current_mode = "-d"
            continue
        if argument == "-f":
            current_mode = "-f"
            continue
        if current_mode == "-d":
            directory_parts.append(argument)
        if current_mode == "-f":
            file_name = argument

    return directory_parts, file_name


def create_directories(directory_parts: List[str]) -> str:
    if not directory_parts:
        return ""
    path: str = os.path.join(*directory_parts)
    os.makedirs(path, exist_ok=True)
    return path


def read_content() -> List[str]:
    content_lines: List[str] = []
    while True:
        user_input: str = input("Enter content line: ")
        if user_input == "stop":
            break
        content_lines.append(user_input)
    return content_lines


def write_file(file_path: str, content_lines: List[str]) -> None:
    file_exists: bool = os.path.exists(file_path)
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as target_file:
        if file_exists:
            target_file.write("\n")
        target_file.write(f"{timestamp}\n")
        for index, line in enumerate(content_lines, start=1):
            target_file.write(f"{index} {line}\n")


def create_file_app() -> None:
    arguments: List[str] = sys.argv[1:]
    directory_parts, file_name = parse_arguments(arguments)
    directory_path: str = create_directories(directory_parts)

    if file_name:
        file_path: str = os.path.join(directory_path, file_name)\
            if directory_path else file_name
        content_lines: List[str] = read_content()
        write_file(file_path, content_lines)


create_file_app()
