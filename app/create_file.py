import os.path
import sys
from datetime import datetime
from os.path import exists


def sort_args(args: list) -> dict:
    result = {"path_parts": [], "file_parts": []}

    if "-d" in args:
        dir_idx = args.index("-d")
        result["path_parts"] = args[dir_idx + 1:]

    if "-f" in args:
        file_idx = args.index("-f")
        result["file_parts"] = args[file_idx + 1:]

    if not result["path_parts"] and not result["file_parts"]:
        exit("No args given")

    return result


def create_full_file_path(file_path: str, file_name_parts: list) -> str:
    if len(file_name_parts) > 1:
        filename = ".".join(file_name_parts)
    else:
        filename = file_name_parts[0]

    if not exists(file_path):
        os.makedirs(file_path, exist_ok=True)

    return os.path.join(file_path, filename)


def open_fill_file(full_file_name: str) -> None:
    is_file_exist = exists(full_file_name)
    with (open(full_file_name, "a")) as file:
        if is_file_exist:
            file.write("\n")

        file.write(f"{datetime.now().strftime('%Y-%m-%D %H:%M:%S')}\n")
        print("You will now fill file content. Enter 'stop' to finish.")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


sorted_args = sort_args(sys.argv[1:])

if len(sorted_args["file_parts"]) == 0:
    exit("No filename provided")

file_dir = str(os.path.join(*sorted_args["path_parts"]))
fullname = create_full_file_path(file_dir, sorted_args["file_parts"])

open_fill_file(fullname)
