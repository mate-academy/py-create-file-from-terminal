import argparse
import os
from datetime import datetime


def create_file() -> None:
    dir_name, file_name = parse_terminal()

    full_name = os.path.join("/".join(dir_name), file_name)
    date = datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    if dir_name:
        os.makedirs("/".join(dir_name), exist_ok=True)

    if file_name:
        with open(os.path.join(full_name), "a") as f:
            f.write(date + "\n")
            index = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                f.write(f"{index} {text}\n")
                index += 1
            f.write("\n")


def parse_terminal() -> tuple:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", type=str, nargs="+", default=[])
    parser.add_argument("-f", type=str, default="")

    args = parser.parse_args()

    return args.d, args.f


create_file()
