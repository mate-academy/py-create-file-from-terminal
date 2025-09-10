import datetime
import os
import sys


arguments = sys.argv


class NoExpectedAttributes(Exception):
    pass


class NoProvidedFolderNames(Exception):
    pass


class NotProvidedFileName(Exception):
    pass


def write_lines_in_file(file_name: str, blank_line: bool) -> None:
    page_number = 1
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")

    with open(file_name, "a") as opened_file:
        if blank_line:
            opened_file.write("\n")

        opened_file.write(current_date)
        new_line = input("Enter content line: ")
        while new_line != "stop":
            opened_file.write(str(page_number) + " " + new_line + "\n")
            new_line = input("Enter content line: ")
            page_number += 1


def write_into_file(file_name: str) -> None:
    if os.path.exists(file_name):
        write_lines_in_file(file_name, True)
    else:
        write_lines_in_file(file_name, False)


def build_and_create_path(folder_names: list[str]) -> None:
    if len(folder_names) == 0:
        raise NoProvidedFolderNames

    new_folder_path = os.path.join(
        os.getcwd(),
        *folder_names
    )

    os.makedirs(new_folder_path, exist_ok=True)


if "-d" not in arguments and "-f" not in arguments:
    print(arguments)
    raise NoExpectedAttributes("Wrong arguments, -f and -d expected")


if "-d" in arguments and "-f" in arguments:
    folder_names = arguments[arguments.index("-d") + 1:arguments.index("-f")]

    try:
        file_name = arguments[arguments.index("-f") + 1]
    except IndexError:
        raise NotProvidedFileName

    filepath = os.path.join(
        os.getcwd(),
        *folder_names,
        file_name
    )

    build_and_create_path(folder_names)
    write_into_file(filepath)
elif "-d" in arguments:
    folder_names = arguments[arguments.index("-d") + 1:]

    build_and_create_path(folder_names)
else:
    try:
        file_name = arguments[arguments.index("-f") + 1]
    except IndexError:
        raise NotProvidedFileName

    file_name = os.path.join(
        os.getcwd(),
        file_name
    )

    write_into_file(file_name)
