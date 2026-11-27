import datetime
import os
import sys


def process_arguments() -> None:
    arguments = sys.argv
    file_index = None
    directory_path: str = ""
    file_name = ""
    if "-f" in arguments:
        file_index = arguments.index("-f")
        file_name = arguments[file_index + 1]

    if "-d" in arguments:
        directory_index = arguments.index("-d")
        if "-f" in arguments and file_index > directory_index:
            directory_names = arguments[directory_index + 1: file_index]
        else:
            directory_names = arguments[directory_index + 1:]

        directory_path = os.path.join("", *directory_names)
        os.makedirs(directory_path, exist_ok=True)
    if "-f" in arguments:
        file_path = os.path.join(directory_path, file_name)
        write_file(file_path)


def write_file(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        if file.tell() > 0:
            file.write("\n")
        today = datetime.datetime.now()
        timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


process_arguments()
