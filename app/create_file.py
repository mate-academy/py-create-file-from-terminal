import sys
import os
from datetime import datetime


def get_content_from_user() -> list:
    content = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.append(current_time)
    number_of_content_line = 1

    while True:
        content_line = input("Enter content line: ")

        if content_line == "stop":
            break

        content.append(f"{number_of_content_line} {content_line}")
        number_of_content_line += 1

    return content


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as new_file:

        for content_line in get_content_from_user():
            new_file.write(f"{content_line} \n")

        new_file.write("\n")


def create_directory(path_to_file: str) -> None:
    os.makedirs(path_to_file, exist_ok=True)


def decode_arguments() -> None:
    arguments = sys.argv[1:]
    path_to_directory = ""
    file_name = None

    if "-d" in arguments:
        index = arguments.index("-d")
        path_to_directory = os.path.join(*arguments[index + 1:])

    elif "-f" in arguments:
        index = arguments.index("-f")
        file_name = arguments[index + 1]
        arguments.remove("-f")
        arguments.remove(file_name)

    if path_to_directory:
        create_directory(path_to_directory)

    if file_name:
        file_path = os.path.join(path_to_directory, file_name)
        create_file(file_path)


if __name__ in "__main__":
    decode_arguments()
