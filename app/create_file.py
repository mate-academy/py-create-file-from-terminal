import os.path
import sys
from datetime import datetime


def make_dir() -> str:
    directory = ""
    for i in range(sys.argv.index("-d") + 1, len(sys.argv)):
        if sys.argv[i] == "-f":
            break
        directory = os.path.join(directory, sys.argv[i])
    os.makedirs(directory, exist_ok=True)

    return directory


def create_file(file_name: str) -> None:
    with (open(os.path.join(file_name), "a") as file):
        file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n")
        line_counter = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{line_counter} {line_content} \n")
            line_counter += 1


if len(sys.argv) > 2:
    if "-d" in sys.argv and "-f" in sys.argv:

        create_file(os.path.join(make_dir(),
                                 sys.argv[sys.argv.index("-f") + 1]))
    elif "-d" in sys.argv:
        make_dir()

    elif "-f" in sys.argv:
        create_file(sys.argv[sys.argv.index("-f") + 1])
