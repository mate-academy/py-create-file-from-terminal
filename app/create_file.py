import sys
import os
from datetime import datetime

args = sys.argv


def file_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")


def write_to_file(file_path: str) -> None:
    text = input("Enter content line: ")
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) != 0:
            file.write("\n")
        current_date = file_time()
        file.write(current_date)
        count = 0
        while text != "stop":
            count += 1
            file.write(f"{count} {text}\n")
            text = input("Enter content line: ")


if "-d" in args and "-f" not in args:
    path = os.path.join(*args[2:])
    os.makedirs(path, exist_ok=True)

elif "-f" in args and "-d" not in args:
    path = args[2]
    write_to_file(path)


elif "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")

    if d_index < f_index:
        directories_path = args[d_index + 1:f_index]
        file_name = args[f_index + 1]

    elif d_index > f_index:
        directories_path = args[d_index + 1:]
        file_name = args[f_index + 1]

    path = os.path.join(*directories_path)
    os.makedirs(path, exist_ok=True)

    full_path = os.path.join(path, file_name)
    write_to_file(full_path)
