import sys
import os
import datetime


def create_folders(folders) -> str:
    path = os.getcwd()
    if "-f" in folders:
        for folder in folders[folders.index("-d") + 1:folders.index("-f")]:
            path = os.path.join(path, folder)
    else:
        for folder in folders[folders.index("-d") + 1:len(folders)]:
            path = os.path.join(path, folder)
    if os.path.exists(path):
        return path
    os.makedirs(path)


def create_and_write_to_file(argv: list, file_name: str) -> None:
    now = datetime.datetime.now()
    input_text = now.strftime("%Y-%m-%d %H:%M:%S\n")
    while True:
        line = input()
        if line == "stop":
            with open(
                    os.path.join(create_folders(argv), file_name),
                    "a+"
            ) as target_file:
                target_file.write(f"{input_text}\n")
                break
        input_text += f"{line}\n"


if "-d" in sys.argv:
    create_folders(sys.argv)
if "-f" in sys.argv:
    file_name_index = sys.argv[sys.argv.index("-f") + 1]
    create_and_write_to_file(sys.argv, file_name_index)
