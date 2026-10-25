import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    current_flag = None

    for argument in arguments:
        if argument in ("-d", "-f"):
            current_flag = argument
            continue

        if current_flag == "-d":
            directories.append(argument)
        elif current_flag == "-f" and file_name is None:
            file_name = argument

    return directories, file_name


def read_content() -> list[str]:
    content = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)

    return content


def append_content(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {line}"
        for line_number, line in enumerate(content, start=1)
    ]
    entry = "\n".join([timestamp, *numbered_lines])
    separator = ""

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        separator = "\n\n"

    with open(file_path, "a", encoding="utf-8") as source_file:
        source_file.write(separator + entry)


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(directory_path, file_name)
        append_content(file_path, read_content())


main()
