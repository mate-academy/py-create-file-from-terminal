import sys
import os
from typing import Any
from datetime import datetime


def parse(args: list) -> Any:
    directory_parts = []
    file_name = None
    index = 1
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and args[index] != "-f":
                directory_parts.append(args[index])
                index += 1
        elif args[index] == "-f":
            index += 1
            if index < len(args):
                file_name = args[index]
                index += 1
        else:
            index += 1
    return directory_parts, file_name


def content_lines() -> Any:
    lines = []
    count = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{count} {line}")
        count += 1
    return lines


def write(file_path: Any, lines: list) -> None:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(f"{time}\n")
        for line in lines:
            output_file.write(f"{line}\n")


def main() -> Any:
    dir_ls, file_name = parse(sys.argv)
    if dir_ls:
        dir_path = os.path.join(*dir_ls)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        lines = content_lines()
        write(file_path, lines)
