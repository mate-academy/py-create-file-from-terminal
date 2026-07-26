import os
import sys
from datetime import datetime


def parse_arguments(input_string: list) -> tuple:
    dirs = []
    dir_exist = False
    file_name = ""
    file_name_exist = False

    for arg in input_string:
        if (arg == "-d"):
            dir_exist = True
        if (arg == "-f"):
            dir_exist = False
            file_name_exist = True
        if (dir_exist and arg != "-d"):
            dirs.append(arg)
        if (file_name_exist and arg != "-f"):
            file_name = arg
            file_name_exist = False

    return dirs, file_name


def building_directory(actual_directory: str, dirs: list) -> str:
    for dir_part in dirs:
        actual_directory = os.path.join(actual_directory, dir_part)
    if (not os.path.exists(actual_directory)):
        os.makedirs(actual_directory)
    return actual_directory


def building_file(new_file: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    number = 1
    with (open(new_file, "a") as output_file):
        if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
            output_file.write("\n")
        output_file.write(timestamp + "\n")
        for line in lines:
            output_file.write(str(number) + " ")
            output_file.write(line + "\n")
            number += 1


def main() -> None:
    input_string = sys.argv[1:]
    dirs, file_name = parse_arguments(input_string)

    actual_directory = os.getcwd()
    actual_directory = building_directory(actual_directory, dirs)

    if (file_name == ""):
        return
    else:
        new_file = os.path.join(actual_directory, file_name)

    building_file(new_file)


if __name__ == "__main__":
    main()
