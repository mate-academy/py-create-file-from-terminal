import argparse
import os
from datetime import datetime


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="directories", nargs="*", default=[])
    parser.add_argument("-f", dest="file_name")
    arguments = parser.parse_args()

    if not arguments.directories and arguments.file_name is None:
        parser.error("provide a directory with -d or a file name with -f")

    return arguments


def get_content_lines() -> list[str]:
    content_lines = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)
    return content_lines


def append_content(file_path: str, content_lines: list[str]) -> None:
    with open(file_path, "a+", encoding="utf-8") as file:
        file.seek(0)
        existing_content = file.read()
        if existing_content:
            if not existing_content.endswith("\n"):
                file.write("\n")
            if not existing_content.endswith("\n\n"):
                file.write("\n")

        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for line_number, content_line in enumerate(content_lines, start=1):
            file.write(f"{line_number} {content_line}\n")


def main() -> None:
    arguments = get_arguments()
    directory_path = (
        os.path.join(*arguments.directories) if arguments.directories else ""
    )
    if arguments.directories:
        os.makedirs(directory_path, exist_ok=True)

    if arguments.file_name is None:
        return

    file_path = os.path.join(directory_path, arguments.file_name)
    content_lines = get_content_lines()
    append_content(file_path, content_lines)


main()
