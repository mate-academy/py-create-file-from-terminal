import os
import sys
from datetime import datetime


def creating_dir_and_file(dir_path: str, file_name: str) -> None:
    full_path = os.path.join(dir_path, file_name)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    creating_file(full_path)


def creating_file(file_name: str) -> None:
    data = []
    date_now = get_timestamp()

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        data.append(line)

    with open(file_name, "a") as file:
        file.write(date_now + "\n")
        for index, line in enumerate(data):
            index += 1
            file.write(f"{index} {line}\n")
        file.write("\n")


def creating_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")

        dir_path = os.path.join(sys.argv[d_index + 1], sys.argv[d_index + 2])
        file_name = sys.argv[f_index + 1]

        creating_dir_and_file(dir_path, file_name)

    elif "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_path = os.path.join(sys.argv[d_index + 1], sys.argv[d_index + 2])
        creating_dir(dir_path)

    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        creating_file(file_name)
