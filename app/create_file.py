from datetime import datetime
import os
import sys


def create_dirs(path: sys) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file_from_input(dir_path: str, file_name: str) -> None:
    with open(os.path.join(dir_path, file_name), "w") as file:
        content_lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        while True:
            line = input("Enter content line:")

            if line.lower() == "stop":
                break
            else:
                content_lines.append(line)

        file.write("\n".join(content_lines))


def create_file() -> None:
    dir_path = ""
    file_name = ""

    dir_creating = False
    file_creating = False

    for arg in sys.argv[1:]:
        if arg == "-d":
            dir_creating = True
            file_creating = False

            continue

        elif arg == "-f":
            dir_creating = False
            file_creating = True

            continue

        if dir_creating:
            dir_path = os.path.join(dir_path, arg)

        if file_creating:
            file_name = arg

    if dir_path:
        create_dirs(dir_path)

    if file_creating:
        create_file_from_input(dir_path, file_name)


create_file()
