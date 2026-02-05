import datetime
import sys
import os
from typing import TextIO


def get_dir() -> str:
    path = []
    if "-d" in sys.argv and "-f" in sys.argv:
        for i in range(sys.argv.index("-d") + 1, sys.argv.index("-f")):
            path.append(sys.argv[i])

        return str(os.path.join(*path))

    for i in range(sys.argv.index("-d") + 1, len(sys.argv)):
        path.append(sys.argv[i])

    return str(os.path.join(*path))


def get_file_name() -> str:
    return sys.argv[sys.argv.index("-f") + 1]


def create_dir() -> None:
    if not os.path.exists(get_dir()):
        os.makedirs(get_dir(), exist_ok=True)


def get_time() -> str:
    current_time = datetime.datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


def write_user_lines(target_file: TextIO) -> None:
    target_file.write(f"{get_time()}\n")
    count = 1
    while True:
        text = input("Enter content line: ")
        if text.lower() == "stop":
            break
        target_file.write(f"{count} {text}\n")
        count += 1


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_dir()
        with open(os.path.join(get_dir(), get_file_name()), "a") as file:
            write_user_lines(file)
            file.write("\n")
    elif "-d" in sys.argv and "-f" not in sys.argv:
        create_dir()

    elif "-d" not in sys.argv and "-f" in sys.argv:
        with open(get_file_name(), "a") as file:
            write_user_lines(file)
            file.write("\n")
