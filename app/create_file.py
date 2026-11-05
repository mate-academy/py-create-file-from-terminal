import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    directories = []
    file_name = None
    mode = None

    for arg in args:
        if arg in ("-d", "-f"):
            mode = arg
        elif mode == "-d":
            directories.append(arg)
        elif mode == "-f" and file_name is None:
            file_name = arg

    return directories, file_name


def get_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file() -> None:
    directories, file_name = parse_args(sys.argv[1:])

    if not directories and not file_name:
        print("Use -d for directories and/or -f for file name")
        return

    path = ""
    if file_name:
        file_path = os.path.join(path, file_name)
        content = get_content()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_exists = (
            os.path.exists(file_path) and os.path.getsize(file_path) > 0
        )

        with open(file_path, "a") as file:
            if file_exists:
                file.write("\n")
            file.write(timestamp + "\n")
            for number, line in enumerate(content, start=1):
                file.write(f"{number} {line}\n")


if __name__ == "__main__":
    create_file()
    # write your code here
