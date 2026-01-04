import os
import sys
from datetime import datetime


def parse_arguments(input_string: list) -> tuple:
    dirs = []
    dir_exist = False
    file_name = ""
    file_name_exist = False

    for i in input_string:
        if (i == "-d"):
            dir_exist = True
        if (i == "-f"):
            dir_exist = False
            file_name_exist = True
        if (dir_exist and i != "-d"):
            dirs.append(i)
        if (file_name_exist and i != "-f"):
            file_name = i
            file_name_exist = False

    return dirs, file_name


def building_directory(actual_directory: str, dirs: list) -> None:
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
    with (open(new_file, "a") as f):
        if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for line in lines:
            f.write(str(number) + " ")
            f.write(line + "\n")
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
