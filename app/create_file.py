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


def write_lines_in_file(
    file_name: str,
    user_data: str,
    blank_line: bool
) -> None:
    page_number = 1
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")

    with open(file_name, "a") as opened_file:
        if blank_line:
            opened_file.write("\n")

        opened_file.write(current_date)
        for line in user_data:
            opened_file.write(f"{page_number} " + line + "\n")
            page_number += 1


def write_into_file(file_name: str) -> None:
    user_data = ""

    new_line = input("Enter content line: ")

    while new_line != "stop":
        user_data += new_line
        new_line = input("Enter content line: ")

    if os.path.exists(file_name):
        write_lines_in_file(file_name, user_data, True)
    else:
        write_lines_in_file(file_name, user_data, False)


def build_path(folder_names: list[str]) -> str:
    if len(folder_names) == 0:
        raise NoProvidedFolderNames

    return os.path.join(
        os.getcwd(),
        *folder_names
    )


def create_directories(new_folder_path: str) -> None:
    os.makedirs(new_folder_path, exist_ok=True)


def main_function() -> None:
    if "-d" not in arguments and "-f" not in arguments:
        raise NoExpectedAttributes("Wrong arguments, -f and -d expected")

    if "-d" in arguments and "-f" in arguments:
        if arguments.index("-d") < arguments.index("-f"):
            folder_names = arguments[
                arguments.index("-d") + 1
                :arguments.index("-f")
            ]
        else:
            folder_names = arguments[arguments.index("-d") + 1:]

        try:
            file_name = arguments[arguments.index("-f") + 1]
        except IndexError:
            raise NotProvidedFileName

        new_folder_path = build_path(folder_names)

        filepath = os.path.join(
            new_folder_path,
            file_name
        )

        create_directories(new_folder_path)
        write_into_file(filepath)
    elif "-d" in arguments:
        folder_names = arguments[arguments.index("-d") + 1:]

        new_folder_path = build_path(folder_names)
        create_directories(new_folder_path)
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


if __name__ == "__main__":
    main_function()
