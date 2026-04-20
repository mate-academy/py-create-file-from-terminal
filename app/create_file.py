# write your code here
import os
from datetime import datetime
import sys

now = datetime.now()
string_now = now.strftime("%Y-%m-%d %H:%M:%S")
current = os.getcwd()


def create_directory(path: str, current: str) -> str:
    new_dir = os.path.join(current, path)
    os.makedirs(new_dir, exist_ok=True)
    return new_dir


def create_file(file_name: str, current: str, string_now: str) -> None:
    new = os.path.join(current, file_name)
    exist = os.path.exists(new)

    with open(new, "a") as f:
        if exist:
            f.write("\n")
        f.write(string_now + "\n")

        counter = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            counter += 1
            f.write(f"{counter} {content}\n")


args = sys.argv[1:]

has_d = "-d" in args
has_f = "-f" in args

if has_d:
    d_index = args.index("-d")

if has_f:
    f_index = args.index("-f")

if has_d and has_f:
    dir_parts = args[d_index + 1 : f_index]
    file_name = args[f_index + 1]
    path = os.path.join(*dir_parts)
    new_dir = create_directory(path, current)
    create_file(file_name, new_dir, string_now)

elif has_d:
    dir_parts = args[d_index + 1 :]
    path = os.path.join(*dir_parts)
    create_directory(path, current)

elif has_f:
    file_name = args[f_index + 1]
    create_file(file_name, current, string_now)
