import os
import sys
from datetime import datetime
from typing import List, Tuple


def get_arguments() -> Tuple[List[str], str | None]:
    args = sys.argv[1:]
    directories: List[str] = []
    filename: str | None = None
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ["-d", "-f"]:
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return directories, filename


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

    for index, line in enumerate(lines, start=1):
        formatted_lines.append(f"{index} {line}")

    return "\n".join(formatted_lines) + "\n"


def main() -> None:
    directories, filename = get_arguments()

    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    if not filename:
        return

    file_path = os.path.join(path, filename) if path else filename

    lines = get_content_lines()
    content = format_content(lines)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(content)


if __name__ == "__main__":
    main()
