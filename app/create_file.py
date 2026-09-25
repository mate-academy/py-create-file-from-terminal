import sys
import os
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directories = []
    filename = None
    if "-d" in arguments:
        directory_start = arguments.index("-d") + 1
        directory_end = len(arguments)
        if "-f" in arguments and arguments.index("-f") > directory_start - 1:
            directory_end = arguments.index("-f")
        directories = arguments[directory_start:directory_end]
    if "-f" in arguments:
        filename_index = arguments.index("-f") + 1
        if filename_index < len(arguments):
            filename = arguments[filename_index]
    return directories, filename


def collect_content() -> list[str]:
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def write_content(filepath: str, content: list[str]) -> None:
    file_exists = os.path.exists(filepath)
    file_mode = "a" if file_exists else "w"
    with open(filepath, file_mode) as source_file:
        if file_exists:
            source_file.write("\n")
        source_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for line_number, line in enumerate(content, start=1):
            source_file.write(f"{line_number} {line}\n")


directories, filename = parse_arguments(sys.argv[1:])

if directories:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
else:
    directory_path = ""

if filename is not None:
    filepath = os.path.join(directory_path, filename)
    write_content(filepath, collect_content())
