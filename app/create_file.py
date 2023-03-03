import datetime
import os
import sys


def file_from_terminal() -> None:
    directory = sys.argv

    if "-d" in directory and "-f" in directory:
        create_directory(directory[2:-2])
        create_file(directory[-1])
        return

    if "-d" in directory:
        create_directory(directory[2:])

    if "-f" in directory:
        create_file(directory[2])


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.datetime.now().strftime(
            "%y-%m-%d %H:%M:%S\n"))
        count = 0
        while True:
            count += 1
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{count} {text}\n")


def create_directory(directories: list) -> None:
    for directory in directories:
        os.makedirs(directory)
        os.chdir(directory)


if __name__ == "__main__":
    file_from_terminal()
