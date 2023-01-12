import sys
import os
from datetime import datetime


def write_file(path: str) -> None:
    with open(path, "a") as file:
        line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while line != "stop":
            file.write(line + "/n")
            line = input("Enter content line: ")
        file.write("/n")


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def main() -> None:
    args = sys.argv[1:]
    file_path = []
    if "-d" in args and "-f" in args:

        if args[0] == "-d":
            file_path = [arg for arg in args[1:-2]]
            file_path.append(args[1])

        if args[0] == "-f":
            file_path = [arg for arg in args[3:]]
            file_path.append(args[1])

        create_directory(os.path.join(*file_path[:-1]))
        write_file(os.path.join(*file_path))

    elif "-d" in args:
        file_path = [arg for arg in args[1:]]
        create_directory(os.path.join(*file_path))

    elif "-f" in args:
        write_file(args[-1])


if __name__ == "__main__":
    main()
