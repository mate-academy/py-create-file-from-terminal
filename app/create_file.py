import sys
import os
import datetime
from typing import Any


def make_directory(name_dir: str | bytes) -> Any:
    os.makedirs(name_dir, exist_ok=True)
    return name_dir


def create_file(name_file: str | bytes) -> Any:
    content = []
    data = datetime.date.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")

    while True:
        line = input("Enter content line:")
        if line.lower() == "stop":
            break
        content.append(line)
    with open(name_file, "a") as exist_file:
        exist_file.write(f"{data}\n")
        for i, line in enumerate(content):
            exist_file.write(f"{i + 1} {line} \n")
        exist_file.write("\n")


data_file = sys.argv[1:]
print(data_file)

if "-f" not in data_file:
    make_directory(os.path.join(*data_file[1:]))
elif "-d" not in data_file:
    create_file(data_file[-1])
elif "-d" and "-f" in data_file:
    if data_file.index("-d") < data_file.index("-f"):
        file_dir = make_directory(os.path.join(*data_file[1:3]))
        file_path = os.path.join(file_dir, data_file[-1])
    else:
        file_dir = make_directory(os.path.join(*data_file[3:]))
        file_path = os.path.join(file_dir, data_file[1])
    create_file(file_path)
