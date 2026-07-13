import os
import sys
from datetime import datetime


def get_flag_values(arguments: list[str], flag: str) -> list[str]:
    if flag not in arguments:
        return []

    start = arguments.index(flag) + 1
    values = []
    for argument in arguments[start:]:
        if argument in ("-d", "-f"):
            break
        values.append(argument)
    return values


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def append_entry(file_path: str, lines: list[str]) -> None:
    needs_separator = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {line}"
        for line_number, line in enumerate(lines, start=1)
    ]
    entry = "\n".join([timestamp, *numbered_lines])

    with open(file_path, "a") as source_file:
        if needs_separator:
            source_file.write("\n\n")
        source_file.write(entry)


def main() -> None:
    arguments = sys.argv[1:]
    directories = get_flag_values(arguments, "-d")
    file_values = get_flag_values(arguments, "-f")

    directory_path = os.path.join(*directories) if directories else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_values:
        file_path = os.path.join(directory_path, file_values[0])
        append_entry(file_path, read_content())


main()
