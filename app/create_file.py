import os
import sys
from datetime import datetime


def create_directory(path: list[str]) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(name: str) -> None:
    with open(name, "+a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        count = 0
        while True:
            count += 1
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write("\n" + f"{count} " + line)
        f.write("\n\n")


def handle_command() -> None:
    args = sys.argv
    if "-d" in args and "-f" in args:
        dir_path = args[args.index("-d") + 1:args.index("-f")]
        file_name = args[args.index("-f") + 1:][0]
        create_directory(dir_path)
        create_file(os.path.join(*dir_path, file_name))
    if "-d" not in args and "-f" in args:
        file_name = args[args.index("-f") + 1:][0]
        create_file(file_name)
    if "-d" in args and "-f" not in args:
        dir_path = args[args.index("-d") + 1:]
        create_directory(dir_path)


if __name__ == "__main__":
    handle_command()
