import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(arguments: List[str]) -> Tuple[List[str], Optional[str]]:
    directory_parts: List[str] = []
    filename: Optional[str] = None
    current_mode: Optional[str] = None

    for item in arguments:
        if item == "-d":
            current_mode = "dir"
            continue
        if item == "-f":
            current_mode = "file"
            continue

        if current_mode == "dir":
            directory_parts.append(item)
        elif current_mode == "file":
            if filename is None:
                filename = item

    return directory_parts, filename


def read_content_lines() -> List[str]:
    lines: List[str] = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)
    return lines


def build_block(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    numbered_lines: List[str] = []
    for index, line in enumerate(lines, start=1):
        numbered_lines.append(f"{index} {line}")

    return "\n".join([timestamp] + numbered_lines) + "\n"


def ensure_directory(directory_path: str) -> None:
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)


def write_block(file_path: str, block_text: str) -> None:
    file_exists = os.path.exists(file_path)

    if file_exists:
        with open(file_path, "r", encoding="utf-8") as reader:
            existing_content = reader.read()

        needs_separator = existing_content.strip() != ""

        with open(file_path, "a", encoding="utf-8") as writer:
            if needs_separator:
                writer.write("\n")
            writer.write(block_text)
        return

    with open(file_path, "w", encoding="utf-8") as writer:
        writer.write(block_text)


def main() -> None:
    arguments = sys.argv[1:]
    directory_parts, filename = parse_arguments(arguments)

    directory_path = ""
    if directory_parts:
        directory_path = os.path.join(*directory_parts)

    # Requirement: if only -d is passed, create directory and exit successfully
    if directory_parts and filename is None:
        ensure_directory(directory_path)
        return

    # If no filename and no directory parts -> invalid input
    if filename is None:
        print("Error: You must provide a file name using -f flag.")
        print("Example: python create_file.py -f file.txt")
        print("Example: python create_file.py -d dir1 dir2 -f file.txt")
        return

    ensure_directory(directory_path)

    if directory_path:
        file_path = os.path.join(directory_path, filename)
    else:
        file_path = filename

    content_lines = read_content_lines()
    block_text = build_block(content_lines)
    write_block(file_path, block_text)


if __name__ == "__main__":
    main()
