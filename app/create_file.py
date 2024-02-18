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

    if "-d" in sys.argv:
        directories = []
        index_dir = sys.argv.index("-d") + 1

        for i in range(index_dir, len(sys.argv)):
            if sys.argv[i] == "-f":
                break
            directories.append(sys.argv[i])

        directories_path = os.path.join(*directories)
        create_directory(directories_path)
        print(directories_path)

    if "-f" in sys.argv:
        file_name = []
        index_file = sys.argv.index("-f") + 1

        for i in range(index_file, len(sys.argv)):
            if sys.argv[i] == "-d":
                break
            file_name.append(sys.argv[i])

        if "-d" in sys.argv:
            file_name_path = os.path.join(*directories, *file_name)
        else:
            file_name_path = os.path.join(*file_name)
        create_file(file_name_path)


if __name__ == "__main__":
    creating_file_and_directory_in_terminal()
