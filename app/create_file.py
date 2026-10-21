import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    index = 0

    while index < len(arguments):
        option = arguments[index]
        if option == "-d":
            index += 1
            while (
                index < len(arguments)
                and not arguments[index].startswith("-")
            ):
                directories.append(arguments[index])
                index += 1
            continue
        if option == "-f":
            if file_name is not None or index + 1 >= len(arguments):
                raise ValueError(
                    "-f must be followed by one file name"
                )
            file_name = arguments[index + 1]
            index += 2
            continue
        raise ValueError(f"Unknown option or misplaced argument: {option}")

    if not directories and file_name is None:
        raise ValueError(
            "Provide -d with directories, -f with a file, or both"
        )
    return directories, file_name


def read_content_lines() -> list[str]:
    content_lines = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)
    return content_lines


def append_file_content(file_path: str, content_lines: list[str]) -> None:
    if not content_lines:
        return

    file_exists = os.path.exists(file_path)
    with open(file_path, "a", encoding="utf-8", newline="\n") as destination:
        if file_exists and os.path.getsize(file_path) > 0:
            destination.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        destination.write(f"{timestamp}\n")
        for line_number, content_line in enumerate(content_lines, start=1):
            destination.write(f"{line_number} {content_line}\n")


def main() -> None:
    try:
        directories, file_name = parse_arguments(sys.argv[1:])
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return

    directory_path = os.path.join(*directories) if directories else ""
    if directories:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    file_path = (
        os.path.join(directory_path, file_name)
        if directory_path
        else file_name
    )
    append_file_content(file_path, read_content_lines())


main()
