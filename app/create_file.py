from datetime import datetime
import os
from sys import argv


def create_directory() -> str:
    directories = []

    for value in range(argv.index("-d") + 1, len(argv)):
        if argv[value] == "-f":
            break

        directories.append(argv[value])

    current_path = ""

    if directories:
        current_path = os.path.join(*directories)

        if not os.path.exists(current_path):
            os.makedirs(current_path)

    return current_path


def create_file(path: str) -> None:
    file_name = argv[argv.index("-f") + 1]

    if file_name:
        with open(os.path.join(path, file_name), "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

            line_number = 1

            while True:
                entered_content = input("Enter content line: ")

                if entered_content == "stop":
                    break

                file.write(f"{line_number} {entered_content}\n")
                line_number += 1


if "-d" not in argv and "-f" not in argv:
    raise Exception("You should provide at least one flag")

final_path = ""

if "-d" in argv:
    final_path = create_directory()
if "-f" in argv:
    create_file(final_path)
