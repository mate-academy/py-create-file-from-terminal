import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directories: list[str] = []
    filename: str | None = None
    index = 0

    while index < len(args):
        token = args[index]

        if token == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                directories.append(args[index])
                index += 1
            continue

        if token == "-f":
            index += 1
            if index < len(args):
                filename = args[index]
                index += 1
            continue

        index += 1

    return directories, filename


def get_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        lines.append(content_line)
    return lines


def write_content(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{index} {line}"
        for index, line in enumerate(lines, start=1)
    ]
    content_block = "\n".join([timestamp, *numbered_lines])

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n\n" + content_block)
    else:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content_block)


def main() -> None:
    directories, filename = parse_args(sys.argv[1:])

    target_dir = os.path.join(*directories) if directories else "."
    if directories:
        os.makedirs(target_dir, exist_ok=True)

    if filename is None:
        return

    file_path = os.path.join(target_dir, filename)
    content_lines = get_content_lines()
    write_content(file_path, content_lines)


if __name__ == "__main__":
    main()
