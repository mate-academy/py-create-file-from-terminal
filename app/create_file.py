from typing import Optional
import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[str, Optional[str]]:
    folder_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                folder_parts.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
            i += 2
            continue

        i += 1

    folder = os.path.join(*folder_parts) if folder_parts else "."
    return folder, file_name


def get_content() -> list[str]:
    lines = []

    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        lines.append(text)

    return lines


def format_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = [timestamp]

    for i, line in enumerate(lines, start=1):
        block.append(f"{i} {line}")

    return "\n".join(block)


def write_file(file_path: str, content: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n\n" + content)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


def main() -> None:
    args = sys.argv[1:]

    folder, file_name = parse_args(args)

    os.makedirs(folder, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(folder, file_name)

    lines = get_content()
    content = format_content(lines)

    write_file(file_path, content)


main()
