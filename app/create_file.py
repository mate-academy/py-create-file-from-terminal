import os
import sys
from datetime import datetime


def get_content_lines() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def build_text(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"{timestamp}\n"

    for index, line in enumerate(lines, start=1):
        text += f"{index} {line}\n"

    return text


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and args[d_index] not in ("-d", "-f"):
            directory_parts.append(args[d_index])
            d_index += 1

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    return directory_parts, file_name


def main() -> None:
    args = sys.argv[1:]
    directory_parts, file_name = parse_args(args)

    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = "."

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    lines = get_content_lines()
    text = build_text(lines)

    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(text)
    else:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)


main()
