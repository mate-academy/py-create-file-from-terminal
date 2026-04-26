import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directory_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return directory_parts, file_name


def get_content_from_user() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def build_file_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"
    for index, line in enumerate(lines, start=1):
        content += f"{index} {line}\n"
    return content.rstrip("\n")


def main() -> None:
    args = sys.argv[1:]
    directory_parts, file_name = parse_args(args)

    if directory_parts:
        dir_path = os.path.join(*directory_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name:
        file_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )
        lines = get_content_from_user()
        content = build_file_content(lines)

        file_exists = (
            os.path.exists(file_path) and os.path.getsize(file_path) > 0
        )
        with open(file_path, "a") as f:
            if file_exists:
                f.write("\n\n")
            f.write(content)


main()
