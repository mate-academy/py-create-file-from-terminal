import os
import sys
from datetime import datetime


def get_flag_values(arguments: list[str], flag: str) -> list[str]:
    if flag not in arguments:
        return []

    values = []
    flag_index = arguments.index(flag) + 1

    for argument in arguments[flag_index:]:
        if argument.startswith("-"):
            break
        values.append(argument)

    return values


def read_content_lines() -> list[str]:
    content_lines = []

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)

    return content_lines


def write_file(file_path: str, content_lines: list[str]) -> None:
    should_add_blank_line = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as source_file:
        if should_add_blank_line:
            source_file.write("\n\n")

        source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for line_number, content_line in enumerate(content_lines, start=1):
            source_file.write(f"\n{line_number} {content_line}")


def main() -> None:
    arguments = sys.argv[1:]
    directories = get_flag_values(arguments, "-d")
    file_names = get_flag_values(arguments, "-f")

    directory_path = os.path.join(*directories) if directories else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_names:
        file_path = os.path.join(directory_path, file_names[0])
        write_file(file_path, read_content_lines())


main()
