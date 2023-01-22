import sys
import os
from datetime import datetime


def add_info() -> str:
    line_num = 0
    text = ""
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        line_num += 1
        text += f"{line_num} {line}\n"
    return text


path = os.getcwd()
if "-d" in sys.argv:
    for i in range(sys.argv.index("-d") + 1, len(sys.argv)):
        if sys.argv[i] == "-f":
            break
        path = os.path.join(path, sys.argv[i])
    os.makedirs(path, exist_ok=True)
if "-f" in sys.argv:
    path = os.path.join(path, sys.argv[sys.argv.index("-f") + 1])

now = datetime.now()
now_string = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")

if not os.path.exists(path):
    with open(path, "w") as new_file:
        new_file.write(now_string + "\n")
        new_file.write(add_info())
elif "-f" in sys.argv:
    with open(path, "a") as existing_file:
        existing_file.write(f"\n{now_string}\n")
        existing_file.write(add_info())
