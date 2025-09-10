import datetime
import os
import sys


arguments = sys.argv


class NoExpectedAttributes(Exception):
    def __str__(self) -> str:
        return "Expected attributes are not provided"


def write_lines_in_file(file_name: str, blank_line: bool) -> None:
    page_number = 1
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")

    with open(file_name, "a") as opened_file:
        if blank_line:
            opened_file.write("\n")

        opened_file.write(current_date)
        new_line = input("Enter content line: ")
        while new_line != "close":
            opened_file.write(str(page_number) + " " + new_line + "\n")
            new_line = input("Enter content line: ")


def write_into_file(file_name: str) -> None:
    if os.path.exists(file_name):
        write_lines_in_file(file_name, True)
    else:
        write_lines_in_file(file_name, False)


if "-d" not in arguments and "-f" not in arguments:
    print(arguments)
    raise NoExpectedAttributes("Wrong arguments, -f and -d expected")


if arguments[1] == "-d" and arguments[-2] == "-f":
    print("FIRST CASE")
    new_folder_path = os.path.join(os.getcwd(), *arguments[2:-2])
    file_name = arguments[-1]

    os.makedirs(new_folder_path)
    filepath = os.path.join(*arguments[2:-2], file_name)
    write_into_file(filepath)
elif arguments[1] == "-d":
    print("SECOND CASE")
    new_folder_path = os.path.join(os.getcwd(), *arguments[2:])

    os.makedirs(new_folder_path)
else:
    print("THIRD CASE")
    file_name = arguments[2]

    write_into_file(file_name)
