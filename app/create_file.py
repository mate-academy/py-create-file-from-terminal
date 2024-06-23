import datetime
import os
import sys


def create_directory_structure(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str, path: str = None) -> None:
    if path is not None:
        full_path = os.path.join(path, file_name)
    else:
        full_path = os.path.join(os.getcwd(), file_name)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    file_exists = os.path.exists(full_path)
    if file_exists:
        file_is_empty = os.path.getsize(full_path) == 0
    else:
        file_is_empty = False

    with open(full_path, "a+") as file_path:
        if file_exists and not file_is_empty:
            file_path.write("\n")
        local = datetime.datetime.now()
        file_path.write(local.strftime("%m-%d-%Y %H:%M:%S\n"))
        while True:
            line = input("Enter content line (type 'stop' to finish): ")
            if line == "stop":
                break
            file_path.write(f"{line}\n")


args = sys.argv
directory_path = None
file_name = None

if "-d" in args:
    index_of_directory = args.index("-d") + 1
    dir_end_index = len(args)
    for flag in ["-f"]:
        if flag in args:
            dir_end_index = min(dir_end_index, args.index(flag))
    directory_path = os.path.join(*args[index_of_directory:dir_end_index])
    create_directory_structure(path=directory_path)

if "-f" in args:
    index_of_file = args.index("-f") + 1
    if index_of_file < len(args):
        file_name = args[index_of_file]
        create_file(file_name=file_name, path=directory_path)
