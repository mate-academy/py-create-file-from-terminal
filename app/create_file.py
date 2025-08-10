import argparse
import os


from datetime import datetime


def make_dir(names_dir: str, path: str = "") -> str:
    for name_dir in names_dir:
        path = os.path.join(path, name_dir)
    os.makedirs(path, exist_ok=True)
    return path


def file_create(name: str, path_to_file: str = "") -> None:
    path_to_file = os.path.join(path_to_file, name)
    if os.path.exists(path_to_file):
        with open(path_to_file, "a") as result_file:
            result_file.write("\n")
    with open(path_to_file, "a") as result_file:
        result_file.write(f"{datetime.now().strftime('%y-%m-%d %H:%M:%S')}\n")
        number = 1
        line = input("Enter content line: ")
        while line != "stop":
            result_file.write(f"{number} {line} \n")
            line = input("Enter content line: ")
            number += 1


def create_file() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", nargs="*",
        help="use -d to set a directory and subdirectory names to create"
    )
    parser.add_argument(
        "-f",
        help="use -f to set a file name to create file with input content "
             "until input stop"
    )

    args = parser.parse_args()

    dir_names = args.d
    file_name = args.f

    if dir_names and file_name:
        file_create(file_name, path_to_file=make_dir(dir_names))
        quit()

    if dir_names:
        make_dir(dir_names)

    if file_name:
        file_create(file_name)


if create_file().__name__ == "__main__":
    create_file()
