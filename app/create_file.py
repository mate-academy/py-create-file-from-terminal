import os
import sys
from datetime import datetime
from typing import List


def write_content(path: str) -> None:
    line_number = 0
    with open(path, "w") as f_in:
        f_in.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        line_number += 1
        with open(path, "a") as f_in:
            f_in.write(f"{line_number} " + line + "\n")


def create_file(args: List[str]) -> None:
    if "-d" in args and "-f" not in args:
        path = os.path.join(*args[2:])
        os.makedirs(path, exist_ok=True)
        return
    if "-f" in args and "-d" not in args:
        path = args[2]
        write_content(path)
        return
    if "-f" in args and "-d" in args:
        dirs = args[2:-2]
        path = os.path.join(*dirs, args[-1])
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        write_content(path)
        return


if __name__ == "__main__":
    create_file(sys.argv)
