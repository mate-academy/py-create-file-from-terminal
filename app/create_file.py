import sys
import os
from datetime import datetime


def create_dir() -> None:
    start_index = sys.argv.index("-d") + 1

    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
        dir_path = os.path.join(*sys.argv[start_index:end_index])
    else:
        dir_path = os.path.join(*sys.argv[start_index:])

    os.makedirs(dir_path, exist_ok=True)


def create_file() -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]

    if "-d" in sys.argv:
        start_index = sys.argv.index("-d") + 1
        end_index = sys.argv.index("-f")
        dir_path = os.path.join(*sys.argv[start_index:end_index])
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    with open(file_path, "a") as file:
        current_time = str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        file.write(current_time + "\n")

        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{line_number} {text}\n")
            line_number += 1
        file.write("\n")


if "-d" in sys.argv:
    create_dir()

if "-f" in sys.argv:
    create_file()
