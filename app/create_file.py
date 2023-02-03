import argparse
import os
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="extend", nargs="+")
    parser.add_argument("-f")
    args = vars(parser.parse_args())
    dir_path = ""

    if args["d"] is not None:
        dir_path = os.path.join(*args["d"])
        os.makedirs(dir_path, exist_ok=True)

    if args["f"] is not None:
        content = [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
        line_number = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                content.append("\n")
                break
            content.append(f"{line_number} {line}\n")
            line_number += 1
        file_path = os.path.join(dir_path, args["f"])
        with open(file_path, "a") as file:
            file.writelines(content)


if __name__ == "__main__":
    create_file()
