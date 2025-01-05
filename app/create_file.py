from sys import argv
import os
from datetime import datetime


directories = []
file_name = None


if '-d' in argv:
    d_index = argv.index('-d') + 1
    while d_index < len(argv) and not argv[d_index].startswith('-'):
        directories.append(argv[d_index])
        d_index += 1

if '-f' in argv:
    f_index = argv.index('-f') + 1
    if f_index < len(argv) and not argv[f_index].startswith('-'):
        file_name = argv[f_index]


def create_file(name: str, file_path: list = []) -> None:
    if file_path:
        name = os.path.join(*directories, name)
    with open(name, "a") as f:
        line_count = 1
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            f.writelines(f"{line_count} {text} \n")


if directories and file_name:
    path = os.path.join(*directories)
    os.makedirs(path)
    create_file(file_name, directories)
elif directories:
    path = os.path.join(*directories)
    os.makedirs(path)
elif file_name:
    create_file(file_name)


