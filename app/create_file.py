import sys
import os
from datetime import datetime
from typing import List, Tuple, LiteralString


def parse_arguments() -> Tuple[List[str], str]:
    args = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        directories = args[d_index + 1:args.index("-f")]\
            if ("-f" in args) else args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return directories, file_name


def create_directories(
        directories: List[str]
) -> LiteralString | str | bytes:
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return ""


def get_file_content() -> List[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_content(
        content_lines: List[str]
) -> Tuple[str, List[str]]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line
                      in enumerate(content_lines)]
    return timestamp, numbered_lines


def write_to_file(
        file_path: str,
        timestamp: str,
        content_lines: List[str]
) -> None:
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(timestamp + "\n")
        for line in content_lines:
            f.write(line + "\n")


def main() -> None:
    directories, file_name = parse_arguments()
    dir_path = create_directories(directories)

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        content_lines = get_file_content()
        timestamp, formatted_content = format_content(content_lines)
        write_to_file(file_path, timestamp, formatted_content)


if __name__ == "__main__":
    main()
