import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Return directory parts and an optional file name from CLI arguments."""
    directories = []
    file_name = None
    current_option = None

    for argument in arguments:
        if argument in ("-d", "-f"):
            current_option = argument
        elif current_option == "-d":
            directories.append(argument)
        elif current_option == "-f":
            if file_name is None:
                file_name = argument
            else:
                raise ValueError("Only one file name can be provided after -f")

    return directories, file_name


def collect_content() -> list[str]:
    """Read content lines until the user enters the stop command."""
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            return content
        content.append(line)


def create_file(path: str) -> None:
    """Append a timestamped, numbered content entry to a file."""
    with open(path, "a+", encoding="utf-8") as destination:
        has_content = os.path.getsize(path) > 0
        content = collect_content()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numbered_lines = [
            f"{number} {line}" for number, line in enumerate(content, 1)
        ]
        entry = "\n".join([timestamp, *numbered_lines])

        if has_content:
            destination.write("\n")
        destination.write(entry + "\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = os.path.join(*directories) if directories else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


main()
