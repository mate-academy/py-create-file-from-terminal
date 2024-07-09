import sys
import os
from datetime import datetime


def create_path(user_input: str) -> str:
    args = user_input.split()

    if "-f" in args:
        file_path = args[args.index("-f") + 1]
    elif "-d" in args:
        dir_path = os.path.join(*args[args.index("-d") + 1:])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "file.txt")
    elif "-d" in args and "-f" in args:
        dir_path = os.path.join(
            *args[args.index("-d") + 1:args.index("-f")]
        )
        file_name = args[args.index("-f") + 1]
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
    else:
        raise ValueError("Invalid arguments")

    return file_path


def main() -> None:
    try:
        file_path = create_path(" ".join(sys.argv[1:]))
    except ValueError as e:
        print(e)
        return

    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode) as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"Line{line_number} {content}\n")
            line_number += 1
