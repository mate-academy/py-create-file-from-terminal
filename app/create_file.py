import sys
import os
from datetime import datetime


def need_directory() -> bool:
    return "-d" in sys.argv


def need_file() -> bool:
    return "-f" in sys.argv


def do_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now}\n")

        line_number = 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

        file.write("\n")


def create_directory(*args) -> None:
    os.makedirs(os.path.join(*args))


def app() -> None:
    target_dir = os.getcwd()

    if need_directory():
        new_dir = sys.argv[
            sys.argv.index("-d") + 1:
            sys.argv.index("-f") if need_file() else None
        ]
        target_dir = os.path.join(target_dir, *new_dir)
        if not os.path.exists(target_dir):
            create_directory(*new_dir)

    if need_file():
        file_path = os.path.join(
            target_dir,
            sys.argv[sys.argv.index("-f") + 1]
        )
        do_file(file_path)


if __name__ == "__main__":
    app()
