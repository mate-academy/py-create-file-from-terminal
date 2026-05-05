import sys
import os
from datetime import datetime


def parse_arguments(
    args: list[str]
) -> tuple[list, str]:
    directories = []
    add_dir = False
    for index, element in enumerate(args):
        if element == "-f":
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
    # Use os.path.join to create path
    # Use os.makedirs with exist_ok=True
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
    for line_no, line in enumerate(lines):
        format_lines.append(" ".join([str(line_no + 1), line]))
    content = "\n".join(format_lines)
    return content


def write_to_file(
    filepath: str,
    content: str
) -> None:
    with open(filepath, "a") as f:
        f.write(content)


def main(
) -> None:
    directories, filename = parse_arguments(sys.argv)
    if any(directories):
        path = create_directories(directories)
        filepath = os.path.join(path, filename)
    else:
        filepath = filename
    lines = get_content_from_user()
    content = format_content(lines)
    write_to_file(filepath, content)


if __name__ == "__main__":
    main()
