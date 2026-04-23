import sys
import os
from datetime import datetime


def create_dirs(stroke_to_parse: sys) -> str:
    current_dir = str(os.getcwd())
    for item in stroke_to_parse:
        if "dir" in item:
            current_dir = os.path.join(current_dir, item)
    os.makedirs(current_dir, exist_ok=True)
    return current_dir


def create_file(file_name: sys) -> None:
    print(file_name)
    count_content_line = 1
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S\n"))
        while True:
            content = input("Enter content line: ")
            file.write(f"{count_content_line} {content}\n")
            count_content_line += 1
            if content == "stop":
                break


def mkdirs_and_file() -> None:
    stroke = sys.argv
    file_name_and_path = os.path.join(
        create_dirs(stroke), stroke[stroke.index("-f") + 1 :][0]
    )
    create_file(file_name_and_path)


if "-d" and "-f" in sys.argv:
    mkdirs_and_file()

if "-f" in sys.argv:
    create_dirs(sys.argv[sys.argv.index("-f") + 1:][0])

if "-d" in sys.argv:
    create_dirs(sys.argv)
