import sys
import os
from datetime import datetime


def make_directory(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def make_file(file_path: str) -> None:
    with open(file_path, "a") as result_file:
        date = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        result_file.write(f"{date}\n")
        line_counter = 1

        while True:
            content = input("Enter content to add to the file: ")

            if content == "stop":
                break

            result_file.write(f"{line_counter} {content}\n")
            line_counter += 1


def main() -> None:
    commands = sys.argv

    if "-d" in commands:

        if "-f" in commands:
            make_directory(commands[2:-2])
            make_file(os.path.join(*commands[2:-2], commands[-1]))

        else:
            make_directory(commands[2:])

    make_file(commands[2])


if __name__ == "__main__":
    main()
