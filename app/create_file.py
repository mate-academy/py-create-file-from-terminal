import datetime
import os
import sys


def create_directory(directories: list) -> None:
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        os.chdir(directory)


def file_naming(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        counter = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{counter} {content_line}\n")
            counter += 1


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_directory(
            sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        )
        file_naming(sys.argv[sys.argv.index("-f") + 1])

    if "-f" not in sys.argv:
        create_directory(sys.argv[sys.argv.index("-d") + 1::])

    if "-d" not in sys.argv:
        file_naming(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    create_file()
