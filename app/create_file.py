import os
import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str)
    parser.add_argument("-d", type=str, nargs="*")
    args = parser.parse_args()
    way = os.getcwd()

    if args.d is not None:
        way = os.path.join(*args.d)
        os.makedirs(way, exist_ok=True)

    if args.f is not None:
        new_way = os.path.join(way, args.f)
        add_content(new_way)
