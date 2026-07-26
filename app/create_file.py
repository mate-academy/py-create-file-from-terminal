import os
import sys
from datetime import datetime


def creating_dir_and_file(dir_path: str, file_name: str) -> None:
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    creating_file(os.path.join(dir_path, file_name))


def creating_file(file_name: str) -> None:
    data = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        data.append(line)

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for index, line in enumerate(data, start=1):
            file.write(f"{index} {line}")
            if index < len(data):
                file.write("\n")


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
        os.makedirs(dir_path, exist_ok=True)

    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        creating_file(file_name)


if __name__ == "__main__":
    create_file()
