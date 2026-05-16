import os
import sys
import datetime


def get_directory_path(arguments: list) -> str:
    if "-d" not in arguments:
        return ""

    start_index = arguments.index("-d") + 1

    directories = []

    for argument in arguments[start_index:]:
        if argument.startswith("-"):
            break

        directories.append(argument)

    return os.path.join(*directories)


def get_file_name(arguments: list) -> str:
    if "-f" not in arguments:
        return ""

    file_index = arguments.index("-f") + 1
    return arguments[file_index]


def get_file_content() -> list:
    file_content = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        file_content.append(line)
    return file_content


def format_content(content_lines: list) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_lines = [timestamp]

    for line_number, line in enumerate(content_lines, start=1):
        formatted_lines.append(f"{line_number} {line}")
    return "\n".join(formatted_lines) + "\n"


def create_directories(path: str) -> None:
    if path:
        os.makedirs(path, exist_ok=True)


def create_file(file_path: str, content: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(content)


def main() -> None:
    arguments = sys.argv[1:]

    directory_path = get_directory_path(arguments)
    file_name = get_file_name(arguments)

    if directory_path:
        create_directories(directory_path)

    if file_name:
        file_content = get_file_content()
        formatted_content = format_content(file_content)

        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        create_file(file_path, formatted_content)


main()
