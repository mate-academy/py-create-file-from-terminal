import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Return directory names and an optional file name from CLI arguments."""
    directories = []
    file_name = None
    index = 0

    while index < len(arguments):
        flag = arguments[index]

        if flag == "-d":
            index += 1
            while index < len(arguments) and arguments[index] not in (
                "-d", "-f"
            ):
                directories.append(arguments[index])
                index += 1
        elif flag == "-f":
            index += 1
            if index < len(arguments) and arguments[index] not in (
                "-d", "-f"
            ):
                file_name = arguments[index]
                index += 1
        else:
            index += 1

    return directories, file_name


def create_file(path: str) -> None:
    """Create or append a timestamped, numbered block of entered lines."""
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = [timestamp]
    block.extend(
        f"{number} {line}" for number, line in enumerate(content_lines, 1)
    )

    has_content = os.path.exists(path) and os.path.getsize(path) > 0
    with open(path, "a", encoding="utf-8") as output_file:
        if has_content:
            output_file.write("\n")
        output_file.write("\n".join(block) + "\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = os.path.join(*directories) if directories else ""

    if directories:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


main()
