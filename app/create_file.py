import os
import sys
from datetime import datetime


def input_cl() -> dict:
    cl = sys.argv[1:]

    directories = []
    filename = ""
    fl_dir = False
    fl_file = False

    for argument in cl:
        if argument == "-d":
            fl_dir = True
            fl_file = False
            continue

        if argument == "-f":
            fl_file = True
            fl_dir = False
            continue

        if fl_dir:
            directories.append(argument)

        if fl_file:
            filename = argument

    return {"dir": directories, "filename": filename}


def create_file() -> None:
    arguments = input_cl()
    directories = arguments["dir"]
    filename = arguments["filename"]

    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if not filename:
        return

    full_path = os.path.join(dir_path, filename) if dir_path else filename

    file_has_content = (
        os.path.exists(full_path) and os.path.getsize(full_path) > 0)

    with open(full_path, "a") as source_file:
        if file_has_content:
            source_file.write("\n")
        source_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    page_number = 0
    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        page_number += 1
        with open(full_path, "a") as source_file:
            source_file.write(f"{page_number} {line}\n")


create_file()
