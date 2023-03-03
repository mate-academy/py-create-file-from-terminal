import datetime
import os
import sys


def file_from_terminal() -> None:
    home_directory = sys.argv

    if "-d" in home_directory and "-f" in home_directory:
        create_directory(home_directory[2:-2])
        create_file(home_directory[-1])
        return

    if "-d" in home_directory:
        create_directory(home_directory[2:])

    if "-f" in home_directory:
        create_file(home_directory[2])


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
        os.mkdir(directory)
        os.chdir(directory)


if __name__ == "__main__":
    file_from_terminal()
