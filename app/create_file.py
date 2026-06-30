import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments() -> Tuple[List[str], Optional[str]]:
    directories: List[str] = []
    filename: Optional[str] = None

    args = sys.argv[1:]
    current_flag: Optional[str] = None

    for i, arg in enumerate(args):
        if arg == "-d":
            if i + 1 >= len(args) or args[i + 1].startswith("-"):
                sys.exit(1)
            current_flag = "-d"
            continue
        elif arg == "-f":
            if i + 1 >= len(args) or args[i + 1].startswith("-"):
                sys.exit(1)
            current_flag = "-f"
            continue

        # Обробка значень (не прапорців)
        if current_flag == "-d":
            directories.append(arg)
        elif current_flag == "-f":
            filename = arg

    return directories, filename


def create_directories(directories: List[str]) -> None:
    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)


def get_content_lines() -> List[str]:
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]
    for line_number, line in enumerate(lines, start=1):
        formatted_lines.append(f"{line_number} {line}")
    return "\n".join(formatted_lines)


def write_to_file(file_path: str, content: str) -> None:
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as source_file:
            source_file.write("\n\n")
            source_file.write(content)
    else:
        with open(file_path, "w", encoding="utf-8") as source_file:
            source_file.write(content)


def main() -> None:
    directories, filename = parse_arguments()

    create_directories(directories)

    if not filename:
        return

    if directories:
        file_path = os.path.join(*directories, filename)
    else:
        file_path = filename

    lines = get_content_lines()
    content = format_content(lines)
    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
else:
    main()
