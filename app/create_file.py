import os
import sys
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    arguments = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in arguments:
        directory_index = arguments.index("-d")

        for argument in arguments[directory_index + 1:]:
            if argument in ("-d", "-f"):
                break

            directories.append(argument)

    if "-f" in arguments:
        file_index = arguments.index("-f")

        if file_index + 1 < len(arguments):
            file_name = arguments[file_index + 1]

    return directories, file_name


def create_directories(directories: list[str]) -> str:
    if not directories:
        return ""

    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def write_content(file_path: str, lines: list[str]) -> None:
    file_has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if file_has_content:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for line_number, line in enumerate(lines, start=1):
            file.write(f"{line_number} {line}\n")


def main() -> None:
    directories, file_name = parse_arguments()
    directory_path = create_directories(directories)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    content = get_content()
    write_content(file_path, content)


main()
