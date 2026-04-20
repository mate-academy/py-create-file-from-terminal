import os
import sys
from datetime import datetime


def create_directory(directory_path: list) -> str:
    path = os.path.join(*directory_path)
    os.makedirs(path, exist_ok=True)
    return str(path)


def create_and_write_file(directory_path: list, file_name: str | list) -> None:
    path = create_directory(directory_path)
    full_path = os.path.join(path, file_name)
    with open(full_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line} {content}\n")
            line += 1


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_and_write_file(sys.argv[
                              sys.argv.index("-d") + 1:
                              sys.argv.index("-f")
                              ],
                              sys.argv[sys.argv.index("-f") + 1])
    elif "-d" in sys.argv:
        create_directory(sys.argv[sys.argv.index("-d") + 1:])
    elif "-f" in sys.argv:
        create_and_write_file(["."], sys.argv[-1])


if __name__ == "__main__":
    create_file()
