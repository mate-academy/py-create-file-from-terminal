import argparse
import os
from datetime import datetime


def create_dirs(d_path: list) -> None:
    os.makedirs(os.path.join(*d_path), exist_ok=True)


def collect_data() -> str:
    info = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    counter = 1
    info.append(f"{current_time}\n")
    while True:
        line_from_user = input("Enter content line: ")
        if line_from_user == "stop":
            info.append("\n")
            break
        info.append(f"{counter} {line_from_user}\n")
        counter += 1
    return "".join(info)


def write_data(file_name: str, path: list = None) -> None:
    file_path = os.path.join(*path, file_name) if path else file_name
    data_from_user = collect_data()
    try:
        with open(file_path, "a") as file:
            file.write(data_from_user)
    except OSError as e:
        print(f"Cannot open/create file: {file}. Error {e}")


def parse_argv() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", type=str)
    parser.add_argument("-d", "--dir_path", type=str, nargs="+")
    sys_args = parser.parse_args()
    file_name = sys_args.file_name
    dir_path = sys_args.dir_path
    return file_name, dir_path


def create_file() -> None:
    file, dirs = parse_argv()
    if file:
        if dirs:
            create_dirs(dirs)
        write_data(file, dirs)
    elif dirs:
        create_dirs(dirs)


if __name__ == "__main__":
    create_file()
