import sys
import os
from datetime import datetime


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    directory_parts = []
    output_file = None
    index = 0

    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                directory_parts.append(args[index])
                index += 1
            continue

        if args[index] == "-f":
            index += 1
            if index < len(args):
                output_file = args[index]
                index += 1
            continue

        index += 1

    return directory_parts, output_file


def create_directory(directory_parts: list[str]) -> str:
    if not directory_parts:
        return ""

    directory_path = os.path.join(*directory_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_content_from_user() -> list[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_content_to_file(full_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_mode = "a" if os.path.exists(full_path) else "w"

    with open(full_path, file_mode, encoding="utf-8") as output_file:
        if file_mode == "a":
            output_file.write("\n")

        output_file.write(f"{timestamp}\n")

        for line_number, line in enumerate(content_lines, start=1):
            output_file.write(f"{line_number} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    directory_parts, output_file = parse_arguments(args)
    if not output_file:
        return

    directory_path = create_directory(directory_parts)
    full_path = (
        os.path.join(directory_path, output_file)
        if directory_path
        else output_file
    )

    content_lines = get_content_from_user()
    write_content_to_file(full_path, content_lines)


if __name__ == "__main__":
    main()
