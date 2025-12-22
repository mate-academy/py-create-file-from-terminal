# write your code here
import os
from datetime import datetime
import sys

now = datetime.now()
string_now = now.strftime("%Y-%m-%d %H:%M:%S")

current = os.getcwd()


def create_directory(path: str, current: str) -> str:
    new_dir = os.path.join(current, path)
    os.makedirs(new_dir)
    return new_dir


def create_file(file_name: str, current: str, string_now: str) -> None:
    new = os.path.join(current, file_name)
    with open(new, "a") as f:
        f.write(string_now)
        counter = 0
        while True:
            counter += 1
            content = input()
            if content == "stop":
                break
            f.write(f"{counter} Line{counter} {content}")


args = sys.argv
if "-d" in args and "-f" in args:
    all_dir = args[2:-2:]
    path = "/".join(all_dir)
    create_file(args[-1], create_directory(path, current), string_now)
elif "-d" in args:
    all_dir = args[2:]
    path = "/".join(all_dir)
    create_directory(path, current)
elif "-f" in args:
    create_file(args[-1], current, string_now)
