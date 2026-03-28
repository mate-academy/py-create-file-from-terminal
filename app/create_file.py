import sys
import os
from datetime import datetime


def fill_file_content(name_file: str) -> None:
    with open(name_file, "a") as new_file:
        time_label = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(time_label + "\n")
        content = ""
        data = ""
        count = 1
        while data != "stop":
            data = input("Enter content line:")
            if data != "stop":
                content += f"{count} " + data + "\n"
                count += 1
        new_file.write(content + "\n")


def create_file(name_file: str) -> None:
    if os.path.isfile(name_file):
        fill_file_content(name_file)
        return
    with open(name_file, "w") as new_file:
        new_file.write("")
    fill_file_content(name_file)


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        if path != "":
            os.makedirs(path)


def create_file_from_terminal() -> None:
    arguments = sys.argv[1:]
    if "-d" in arguments and "-f" in arguments:
        index_flag = arguments.index("-f")
        path = os.path.join(*arguments[1:index_flag])
        name_file = os.path.join(path, arguments[index_flag + 1:][0])
        create_dir(path)
        create_file(name_file)

    elif "-d" in arguments:
        path = os.path.join(*arguments[1:])
        print(path)
        create_dir(path)

    elif "-f" in arguments:
        name_file = arguments[1]
        create_file(name_file)
