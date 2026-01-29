import argparse
import datetime
import os


def create_file(
        name_of_the_file: str,
        create_in_directory: list
) -> None | Exception:

    first_line = datetime.datetime.now()

    if create_in_directory:
        create_in_directory.append(name_of_the_file)
        name_of_the_file = os.path.join(*create_in_directory)

    try:
        with open(name_of_the_file, "a") as creating_file:
            creating_file.write(first_line.strftime("%Y-%m-%d %H:%M:%S\n"))
    except Exception as e_info:
        return e_info

    line_num = 1
    while True:
        content = input("Enter content line: ")

        try:
            with open(name_of_the_file, "a") as editing_file:
                if content == "stop":
                    editing_file.write("\n")
                    break
                editing_file.write(f"{line_num} {content}\n")
                line_num += 1
        except Exception as e_info:
            return e_info


def create_directory(path_to_implement: list) -> None:
    try:
        path = os.path.join(*path_to_implement)
        os.makedirs(path, exist_ok=True)
    except OSError as error_info:
        print(error_info)


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file_name")
parser.add_argument("-d", "--dir_path", nargs="+")

command = parser.parse_args()

if command.dir_path:
    create_directory(command.dir_path)
if command.file_name:
    create_file(command.file_name, command.dir_path)
