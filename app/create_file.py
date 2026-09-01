import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(
    arguments: List[str],
) -> Tuple[List[str], Optional[str]]:
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


def read_content() -> List[str]:
    content_lines = []

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)

    return content_lines


def write_content(file_path: str, content_lines: List[str]) -> None:
    should_add_separator = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {content_line}"
        for line_number, content_line in enumerate(content_lines, start=1)
    ]
    entry = "\n".join([timestamp, *numbered_lines])

    with open(file_path, "a", encoding="utf-8") as source_file:
        if should_add_separator:
            source_file.write("\n\n")
        source_file.write(entry)


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    file_path = (
        os.path.join(directory_path, file_name)
        if directory_path
        else file_name
    )
    write_content(file_path, read_content())


if __name__ in {"__main__", "<run_path>"}:
    main()
