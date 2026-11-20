import os
import sys
from datetime import datetime


def get_arguments() -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    current_flag = None

    for argument in sys.argv[1:]:
        if argument in ("-d", "-f"):
            current_flag = argument
        elif current_flag == "-d":
            directories.append(argument)
        elif current_flag == "-f" and file_name is None:
            file_name = argument

    return directories, file_name


def create_file() -> None:
    directories, file_name = get_arguments()
    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    content_lines = []

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)

    entry_lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    entry_lines.extend(
        f"{line_number} {line}"
        for line_number, line in enumerate(content_lines, start=1)
    )
    entry = "\n".join(entry_lines)

    separator = ""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        separator = "\n\n"

    with open(file_path, "a", encoding="utf-8") as target_file:
        target_file.write(separator + entry)


create_file()
