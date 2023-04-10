import sys
import os
from datetime import datetime


def add_content(way: str) -> None:
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S" + "\n")
    with open(way, "w") as f:
        f.write(timestamp)
    while True:
        with open(way, "a") as f:
            content = input("Enter content line: ")
            f.write(content + "\n")
            if content == "stop":
                break


def create_file() -> None:
    command = sys.argv
    if "-d" not in command:
        way = command[-1]
        add_content(way)

    if "-d" in command:
        if len(command) == 4:
            add_dir = os.path.join(command[-2], command[-1])
            os.makedirs(add_dir, exist_ok=True)

        if len(command) == 6:
            add_dir = os.path.join(command[-4], command[-3])
            os.makedirs(add_dir, exist_ok=True)
            way = os.path.join(command[-4], command[-3], command[-1])
            add_content(way)
