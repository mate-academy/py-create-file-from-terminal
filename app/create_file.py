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

    with open(full_path, "a+") as file_path:
        local = datetime.datetime.now()
        file_path.write(local.strftime("%m-%d-%Y %H:%M:%S\n"))
        while True:
            line = input("Enter content line (type 'stop' to finish): ")
            if line == "stop":
                break
            file_path.write(f"{line}\n")


path_list = sys.argv

if "-d" in path_list and "-f" not in path_list:
    create_directory_structure(path=os.path.join(*path_list[2:]))
elif "-f" in path_list and "-d" not in path_list:
    create_file(file_name=path_list[2])
else:
    path_with_directory = {}
    path_with_file = {}

    index_of_directory = path_list.index("-d")
    index_of_file = path_list.index("-f")

    for element in path_list[2:]:
        path_with_directory = path_list[2:index_of_file]
        path_with_file = path_list[-1]
    create_file(
        file_name=path_with_file,
        path=os.path.join(*path_with_directory)
    )
