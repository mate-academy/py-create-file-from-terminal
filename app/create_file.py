import os
import argparse
from datetime import datetime


def create_directory_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*")
    parser.add_argument("-f", nargs=1)

    args = vars(parser.parse_args())

    create_directory(*args["d"])
    add_content(os.path.join(*args["d"] + args["f"]))


def create_directory(*dirs_path) -> None:
    os.makedirs(os.path.join(*dirs_path), exist_ok=True)


def add_content(*path) -> None:
    current_time = datetime.strftime(datetime.now(), "%Y-%d-%m %H:%M:%S")

    with open(os.path.join(*path), "w") as f:
        f.write(f"{current_time}\n")
        num_line = 0
        content = input("Enter content line:")
        while content.lower() != "stop":
            num_line += 1
            f.write(f"{num_line} Line{num_line} {content}\n")
            content = input("Enter content line:")


create_directory_file()
