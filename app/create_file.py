import os
import sys
from datetime import datetime


PROMPT = "Enter content line: "
STOP_WORD = "stop"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def read_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        user_input = input(PROMPT)
        if user_input == STOP_WORD:
            break
        lines.append(user_input)
    return lines


def append_content_block(file_path: str, lines: list[str]) -> None:
    should_add_blank_line = (os.path.exists(file_path)
                             and os.path.getsize(file_path) > 0)

    with open(file_path, "a", encoding="utf-8") as source_file:
        if should_add_blank_line:
            source_file.write("\n")

        source_file.write(f"{datetime.now().strftime(TIME_FORMAT)}\n")
        for index, line in enumerate(lines, start=1):
            source_file.write(f"{index} {line}\n")


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    directories: list[str] = []
    filename: str | None = None

    if "-d" in args:
        d_index = args.index("-d")
        d_end = len(args)
        if "-f" in args and args.index("-f") > d_index:
            d_end = args.index("-f")
        directories = args[d_index + 1:d_end]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    return directories, filename


def main() -> None:
    args = sys.argv[1:]
    directories, filename = parse_arguments(args)

    target_directory = os.getcwd()
    if directories:
        target_directory = os.path.join(os.getcwd(), *directories)
        os.makedirs(target_directory, exist_ok=True)

    if filename:
        file_path = os.path.join(target_directory, filename)
        content_lines = read_content_lines()
        append_content_block(file_path, content_lines)


main()
