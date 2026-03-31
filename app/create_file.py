import sys
import os

import datetime


def create_directory(directory: list) -> None:
    os.makedirs(os.path.join(*directory), exist_ok=True)


def writing_into_file(path: list) -> None:
    with open(os.path.join(*path), "a") as file:

        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        while True:
            content_line = input("Enter content line:")

            if content_line == "stop":
                file.write("\n")
                break

            string_number = 1
            file.write(str(string_number)
                       + " "
                       + content_line
                       + "\n")
            string_number += 1


if __name__ == "__main__":

    file_directory = []

    if "-d" in sys.argv:
        for element in sys.argv[sys.argv.index("-d") + 1:]:
            if element == "-f":
                break

            file_directory.append(element)
        create_directory(file_directory)

        if "-f" in sys.argv:
            full_file_path = file_directory + [
                sys.argv[sys.argv.index("-f") + 1]
            ]

            writing_into_file(full_file_path)
