import os
import sys

from datetime import datetime


def create_path(directories: list[str]) -> str:
    if len(directories) == 0:
        return "."
    path = os.path.join(*directories)
    return path


def create_directories(directory_path: list["str"]) -> None:
    directories = []
    for element in directory_path[1:]:
        if element == "-f":
            break
        directories.append(element)

    path = create_path(directories)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


def create_and_fulfill_file(directory_path: list["str"]) -> None:
    filename = directory_path[-1]
    with open(filename, "a") as source_file:
        current_date = datetime.now()
        source_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))

        user_input = input("Enter content line: ")
        number_of_line = 1
        while user_input != "stop":
            source_file.write(f"{number_of_line} {user_input}\n")
            number_of_line += 1
            user_input = input("Enter content line: ")
        source_file.write("\n")


def create_file_main() -> None:
    directory_path = sys.argv[1:]
    if len(directory_path) != 0:
        if "-d" in directory_path:
            create_directories(directory_path)

        if "-f" in directory_path:
            create_and_fulfill_file(directory_path)


create_file_main()
