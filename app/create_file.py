import os
import sys

from datetime import datetime as datetime


args = sys.argv[1::]


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
        line_number = 1
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            f.write(f"{line_number} {input_line} \n")
            line_number += 1


def main() -> None:
    if "-d" in args and "-f" in args:
        create_dir(os.path.join(*args[1:-2]))
        create_file(os.path.join(os.path.join(*args[1:-2]), args[-1]))

    elif "-d" in args:
        create_dir(os.path.join(*args[1:]))

    elif "-f" in args:
        create_file(args[1])


if __name__ == "__main__":
    main()
