import argparse
import os
import re
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file with input")

    parser.add_argument("-d", nargs="+", dest="dir_path")
    parser.add_argument("-f", dest="file_name")

    args = parser.parse_args()
    dir_path = args.dir_path
    file_name = args.file_name

    if file_name and not is_valid_name(file_name):
        raise NameError("File name is invalid. Don`t use special symbols!")
    if dir_path and not is_valid_dir_names(dir_path):
        raise NameError("Dir name is invalid. Don`t use special symbols!")

    if dir_path:
        create_dir(dir_path)
    if file_name:
        create_file(file_name, dir_path)


def is_valid_name(name: str) -> bool:
    pattern = re.compile(r"^[a-zA-Z0-9_\-\.]+$")
    return bool(pattern.match(name))


def is_valid_dir_names(dirs_list: list[str]) -> bool:
    return all(is_valid_name(name) for name in dirs_list)


def create_dir(dir_path: list) -> None:
    path = os.path.join(*dir_path)
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str, dir_path: list[str]) -> None:
    if dir_path:
        file_path = os.path.join(*dir_path, file_name)
        data_input(file_path)
    else:
        data_input(file_name)


def collect_data() -> list:
    count = 0
    users_inputs = []
    while True:
        count += 1
        text = input("Enter content line: ")
        if text.lower() == "stop":
            break
        users_inputs.append(f"{count} {text}\n")
    users_inputs.append("\n")
    return users_inputs


def data_input(file_path: str) -> None:
    users_data = collect_data()
    utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file_time:
        file_time.write(f"{utc_time}\n")
        for strings in users_data:
            file_time.write(strings)


if __name__ == "__main__":
    main()
