import os.path
import sys
from datetime import datetime
from os.path import exists


def sort_args(args: list) -> dict:
    result = {
        "path_parts": [],
        "file_parts": []
    }

    dir_idx = 0
    file_idx = 0
    for i in range(len(args)):
        if args[i].lower() == "-d":
            dir_idx = i
        elif args[i].lower() == "-f":
            file_idx = i

    if dir_idx == 0 and file_idx == 0:
        exit("No args given")

    if file_idx == 0:
        result["path_parts"] = args[dir_idx + 1:]
    elif dir_idx == 0:
        result["file_parts"] = args[file_idx + 1:]
    else:
        if dir_idx < file_idx:
            result["path_parts"] = args[dir_idx + 1:file_idx]
            result["file_parts"] = args[file_idx + 1:]
        else:
            result["path_parts"] = args[dir_idx + 1:]
            result["file_parts"] = args[file_idx + 1:dir_idx]

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

        file.write(f"{datetime.now().strftime("%Y-%m-%D %H:%M:%S")}\n")
        print("You will now fill file content. Enter 'stop' to finish.")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


sorted_args = sort_args(sys.argv)

if len(sorted_args["file_parts"]) == 0:
    exit("No filename provided")

file_dir = str(os.path.join(*sorted_args["path_parts"]))
fullname = create_full_file_path(file_dir, sorted_args["file_parts"])

open_fill_file(fullname)
