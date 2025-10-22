import sys
import os
from typing import Any
from datetime import datetime


def parse(args: list) -> Any:
    dir_ls = []
    file_name = None
    i = 1
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_ls.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return dir_ls, file_name


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
    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(f"{time}\n")
        for line in lines:
            f.write(f"{line}\n")


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
