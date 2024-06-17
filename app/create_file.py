import datetime
import os
import sys


def create_argument() -> dict:
    out = {}
    args = sys.argv
    filename = ""
    path = ""

    start_dir = False
    start_file = False

    for arg in args:

        if arg == "-d":
            start_dir = True
            start_file = False
            continue

        if arg == "-f":
            start_dir = False
            start_file = True
            continue

        if start_dir:
            path += arg + "/"

        if start_file:
            filename = arg

    if path:
        out["path"] = path

    if filename:
        out["filename"] = filename

    return out


def create_dir(input_arg: dict) -> str:
    if "path" in input_arg:
        path = os.path.join(input_arg["path"])
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    return ""


def create_file(input_arg: dict) -> None:
    create_dir(input_arg)
    if "filename" not in input_arg:
        return

    input_str = ""
    buff = []

    while input_str != "stop":
        input_str = input("Enter content line:")
        if input_str != "stop":
            buff.append(input_str)

    if not buff:
        return

    file_name_str = create_dir(input_arg) + input_arg["filename"]

    with open(file_name_str, "at") as file:
        current = datetime.datetime.now()
        file.write(current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, data in enumerate(buff):
            file.write(f"{i + 1} {data}\n")


create_file(create_argument())
