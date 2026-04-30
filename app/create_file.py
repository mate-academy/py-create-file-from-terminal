import sys
import os
from typing import Any
from datetime import datetime


def create_path(directories: list) -> Any:
    return os.path.join(os.getcwd(), *directories)


def create_dirs(directories: list) -> Any:
    path = create_path(directories)
    os.makedirs(path, exist_ok=True)


def input_lines() -> None:
    counter = 1
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break

        content_lines.append(f"{counter} {content_line}\n")
        counter += 1


def append_file_content(directories: list,
                        filename: str,
                        input_contents: list
                        ) -> None:
    is_need_space = False
    path = os.path.join(create_path(directories), filename)
    if os.path.exists(path):
        is_need_space = True
    with open(path, "a") as f:
        if is_need_space:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for content in input_contents:
            f.write(content)


flags = ("-f", "-d")
current_flag = None
file_name = None
directories_list = []
content_lines = []

if len(sys.argv) > 2:
    for arg in sys.argv[1:]:
        if arg in flags:
            current_flag = arg
            continue

        if current_flag == "-f":
            file_name = arg
            continue

        if current_flag == "-d":
            directories_list.append(arg)
            continue

    create_dirs(directories_list)
    if file_name:
        input_lines()
        append_file_content(directories_list,
                            file_name,
                            content_lines)
