import sys
import os
from datetime import datetime


def main() -> None:
    parameters = sys.argv[1:]

    if parameters[0] == "-d" and "-f" not in parameters:
        create_directory(parameters[1:])

    if parameters[0] == "-f":
        create_file(parameters[1])

    if parameters[0] == "-d" and "-f" in parameters:
        directory_parts = parameters[1: parameters.index("-f")]
        file_name = parameters[parameters.index("-f") + 1]
        new_file_location = os.path.join(*directory_parts, file_name)
        create_directory(directory_parts)
        create_file(new_file_location)


def create_directory(path_parts: list[str]) -> None:
    dir_name = os.path.join(*path_parts)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def create_file(file_name: str) -> None:
    if os.path.exists(file_name):
        mode = "a"
    else:
        mode = "w"

    with open(file_name, mode) as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 1
        while True:
            text = input("Enter content line: ")

            if text == "stop":
                file.write("\n")
                break

            file.write(f"{line_num} {text}\n")
            line_num += 1


if __name__ == "__main__":
    main()
