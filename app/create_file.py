import os
import sys
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    """Parse CLI arguments and return (directories, file_name).

    Works regardless of whether -d or -f comes first.
    """
    directories = []
    file_name = None

    if "-d" in arguments:
        directory_flag_index = arguments.index("-d")
        for argument in arguments[directory_flag_index + 1:]:
            if argument == "-f":
                break
            directories.append(argument)

    if "-f" in arguments:
        file_flag_index = arguments.index("-f")
        file_name = arguments[file_flag_index + 1]

    return directories, file_name


def create_directories(directories: list) -> str:
    """Create nested directories and return the resulting path."""
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def read_content_lines() -> list:
    """Read lines from the terminal until the user types 'stop'."""
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    return content_lines


def write_content_to_file(file_path: str, content_lines: list) -> None:
    """Append a timestamp and numbered content lines to the file.

    A blank line is placed before a new entry when the file already
    has content, so entries are separated but no trailing blank line
    is left at the end of the file.
    """
    file_exists = os.path.exists(file_path)
    file_has_content = file_exists and os.path.getsize(file_path) > 0
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as target_file:
        if file_has_content:
            target_file.write("\n")
        target_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(content_lines, start=1):
            target_file.write(f"{line_number} {line}\n")


def main() -> None:
    arguments = sys.argv[1:]
    directories, file_name = parse_arguments(arguments)

    directory_path = ""
    if directories:
        directory_path = create_directories(directories)

    if file_name:
        file_path = (
            os.path.join(directory_path, file_name)
            if directory_path
            else file_name
        )
        content_lines = read_content_lines()
        write_content_to_file(file_path, content_lines)
        print(f"File created at: {file_path}")
    elif directories:
        print(f"Directory created at: {directory_path}")


main()
