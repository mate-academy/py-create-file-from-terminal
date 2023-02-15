import os
import sys
from datetime import datetime
from typing import IO


def add_new_content_line(new_file: IO) -> None:
    new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    added_line = ""
    while added_line != "stop":
        added_line = input("Enter content line: ")
        if added_line != "stop":
            new_file.write(f"{added_line}\n")
        else:
            new_file.write("\n")


if "-f" in sys.argv and "-d" not in sys.argv:
    with open(sys.argv[-1], "a") as created_file:
        add_new_content_line(created_file)

if "-d" in sys.argv and "-f" not in sys.argv:
    os.makedirs(os.path.join(*sys.argv[2:]), exist_ok=True)

if "-d" in sys.argv and "-f" in sys.argv:
    os.makedirs(os.path.join(*sys.argv[2:-2]), exist_ok=True)
    sys.argv.remove("-f")
    with open(os.path.join(*sys.argv[2:]), "a") as created_file:
        add_new_content_line(created_file)
