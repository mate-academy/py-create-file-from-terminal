import sys
import os
from datetime import datetime


def parse_arguments(
    args: list[str]
) -> tuple[list[str], str]:
    filename = None
    directories = []
    add_dir = False
    for index, element in enumerate(args):
        if element == "-f":
            if index + 1 < len(args):
                filename = args[index + 1]
            add_dir = False
        elif element == "-d":
            add_dir = True
        elif add_dir:
            directories.append(element)
    return directories, filename


def create_directories(
    directories: list[str]
) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_from_user(
) -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(
    lines: list[str]
) -> str:
    current_date = datetime.now()
    format_lines = [current_date.strftime("%Y-%m-%d %H:%M:%S")]
    format_lines.extend(f"{i + 1} {line}" for i, line in enumerate(lines))
    content = "\n".join(format_lines)
    return content


def write_to_file(
    filepath: str,
    content: str
) -> None:
    if os.path.exists(filepath):
        content = "\n\n" + content

    with open(filepath, "a") as output_file:
        output_file.write(content)


def main(
) -> None:
    directories, filename = parse_arguments(sys.argv)
    path = None
    if any(directories):
        path = create_directories(directories)
    if filename is None:
        return
    if path is None:
        filepath = filename
    else:
        filepath = os.path.join(path, filename)
    lines = get_content_from_user()
    content = format_content(lines)
    write_to_file(filepath, content)


main()
