import os
import sys

from datetime import datetime


def make_directory(directories: list) -> str:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def make_file(file_name: str) -> None:
    with open(os.path.join(file_name), "a") as file:
        date_stamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + "\n"
        file.write(date_stamp)

        line_number = 0
        while True:
            line_number += 1
            content = input(f"Enter content line: ") + "\n"
            if content == "stop\n":
                break
            file.write(line_number, content)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        make_directory(sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")])
        make_directory(sys.argv[sys.argv.index("-f") + 1])

    elif "-d" in sys.argv:
        make_directory(sys.argv[sys.argv.index("-d") + 1:])

    elif "-f" in sys.argv:
        make_file(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    main()
