from typing import Any
import datetime
import os
import sys


def create_file(*args: Any) -> None:

    with open(os.path.join(*args), "a") as file_in:
        file_in.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        count = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file_in.write("\n")
                break
            file_in.write(f"{count} {content}\n")
            count += 1


def create_folder(path: list) -> str:
    os.makedirs(os.path.join(*path), exist_ok=True)
    return os.path.join(*path)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        start_file = sys.argv.index("-f")
        start_folder = sys.argv.index("-d")
        if start_folder < start_file:
            path = create_folder(
                sys.argv[start_folder + 1:start_file]
            )
        else:
            path = create_folder(
                sys.argv[start_folder + 1:]
            )
        file_name = sys.argv[start_file + 1]
        create_file(path, file_name)
    elif "-d" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:]
        create_folder(path)
    elif "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1:]
        create_file(file_name)


if __name__ == "__main__":
    main()
