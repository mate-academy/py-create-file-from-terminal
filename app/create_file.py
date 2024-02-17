import os
import sys
from datetime import datetime


def create_directory(direct: str) -> None:
    if os.path.exists(direct) is not True:
        os.makedirs(direct)


def create_file(name_file: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(name_file, "a") as file:
        file.write(f"{timestamp}\n")
        line_number = 1

        while True:
            content = input("Enter content line: ")
            if content.lower().strip() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1
        file.write("\n")


def creating_file_and_directory_in_terminal() -> None:

    if "-d" in sys.argv and "-f" in sys.argv:
        directories = []
        file_name = []
        index_dir = sys.argv.index("-d") + 1
        index_file = sys.argv.index("-f") + 1

        for i in range(index_dir, len(sys.argv)):
            if sys.argv[i] == "-f":
                break
            directories.append(sys.argv[i])

        for i in range(index_file, len(sys.argv)):
            if sys.argv[i] == "-d":
                break
            file_name.append(sys.argv[i])

        directories_path = os.path.join(*directories)
        file_name_path = os.path.join(*directories, *file_name)
        create_directory(directories_path)
        create_file(file_name_path)

    elif "-d" in sys.argv:
        index_dir = sys.argv.index("-d") + 1
        directories_path = os.path.join(*sys.argv[index_dir:])
        create_directory(directories_path)

    elif "-f" in sys.argv:
        index_file = sys.argv.index("-f") + 1
        file_name_path = os.path.join(*sys.argv[index_file:])
        create_file(file_name_path)


creating_file_and_directory_in_terminal()
