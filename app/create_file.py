from datetime import datetime
import os
from sys import argv


def create_directory() -> str:
    current_path = ""

    if "-d" not in argv:
        return current_path

    directories = []

    for value in range(argv.index("-d") + 1, len(argv)):
        if argv[value] == "-f":
            break

        directories.append(argv[value])

    if directories:
        current_path = os.path.join(*directories)
        os.makedirs(current_path, exist_ok=True)

    return current_path


def create_file() -> None:
    if "-d" not in argv and "-f" not in argv:
        raise Exception("You should provide at least one flag")

    path = create_directory()

    if "-f" not in argv:
        return

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


create_file()
