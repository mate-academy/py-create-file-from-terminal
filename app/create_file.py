import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directories = []
    filename = None
    index = 0

    while index < len(arguments):
        flag = arguments[index]
        index += 1
        if flag == "-d":
            while (index < len(arguments)
                   and not arguments[index].startswith("-")):
                directories.append(arguments[index])
                index += 1
        elif flag == "-f":
            filename = arguments[index]
            index += 1

    return directories, filename


def write_content(file_path: str) -> None:
    with open(file_path, "a+", encoding="utf-8") as file:
        file.seek(0, os.SEEK_END)

        if file.tell() > 0:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1

        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    arguments = sys.argv[1:]

    if not arguments:
        return
    try:
        directories, filename = parse_arguments(arguments)
    except ValueError as error:
        print(error)
        return

    directory_path = os.path.join(*directories) if directories else "."

    if directories:
        os.makedirs(directory_path, exist_ok=True)

    if filename is not None:
        file_path = os.path.join(directory_path, filename)
        write_content(file_path)


main()
