import os
import sys
from datetime import datetime

argv = sys.argv


def parse_arguments() -> tuple:
    folder_path = []
    file_name = None

    if "-d" in argv:
        if "-f" in argv and argv.index("-d") < argv.index("-f"):
            folder_path = argv[argv.index("-d") + 1 : argv.index("-f")]
        else:
            folder_path = argv[argv.index("-d") + 1 :]
    if "-f" in argv:
        file_name = argv[argv.index("-f") + 1]
    return folder_path, file_name


def create_folder(folder_path: list) -> list:
    os.makedirs(os.path.join(*folder_path), exist_ok=True)
    return folder_path


def create_file(folder_path: list, file_name: str) -> None:
    full_path = os.path.join(*folder_path, file_name)
    with open(full_path, "a") as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("\n" + time_now + "\n")
        num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{num} {line}\n")
            num += 1


if __name__ == "__main__":
    folder_path, file_name = parse_arguments()

    if folder_path:
        create_folder(folder_path)
    if file_name:
        create_file(folder_path, file_name)
