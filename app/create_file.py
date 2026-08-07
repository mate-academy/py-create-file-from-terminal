import os
import sys
from datetime import datetime
from typing import List, Optional, Sequence, Tuple


def parse_arguments(args: Sequence[str]) -> Tuple[List[str], Optional[str]]:
    directories = []
    file_name = None

    index = 0
    while index < len(args):
        arg = args[index]
        if arg == "-d":
            index += 1
            while index < len(args) and args[index] != "-f":
                directories.append(args[index])
                index += 1
        elif arg == "-f":
            index += 1
            if index < len(args):
                file_name = args[index]
                index += 1
        else:
            directories.append(arg)
            index += 1

    return directories, file_name


def collect_content() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def build_entry(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{index} {line}" for index, line in enumerate(lines, start=1)
    ]
    return "\n".join([timestamp, *numbered_lines])


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    if directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)

    if file_name is None:
        return

    target_dir = os.path.join(*directories) if directories else "."
    target_path = (
        os.path.join(target_dir, file_name)
        if directories
        else file_name
    )

    content_lines = collect_content()
    entry_text = build_entry(content_lines)

    if os.path.exists(target_path):
        with open(target_path, "r") as source_file:
            existing_content = source_file.read()
        if existing_content.strip():
            new_content = existing_content.rstrip() + "\n\n" + entry_text
        else:
            new_content = entry_text
    else:
        new_content = entry_text

    with open(target_path, "w") as target_file:
        target_file.write(new_content)


main()
