# write your code here
import os
import sys
from datetime import datetime


def open_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


def create_file() -> None:

    if sys.argv[1] == "-f":
        open_file(sys.argv[-1])

    if sys.argv[1] == "-d" and sys.argv[-2] == "-f":
        path = os.path.join(*sys.argv[2:-2])
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, sys.argv[-1])
        open_file(file_path)

    if sys.argv[1] == "-d" and "-f" not in sys.argv:
        os.makedirs(os.path.join(*sys.argv[2:]))
