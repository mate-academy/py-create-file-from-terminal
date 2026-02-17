import os
import sys
import datetime
from typing import Sequence


def create_path(parts: Sequence[str]) -> str:
    return os.path.join(*parts)


def parse_args(argv_to_parse: list[str]) -> tuple[str, list[str]]:
    parsed_file_name = ""
    d_args: list[str] = []
    argv_length = len(argv_to_parse)

    if "-f" in argv_to_parse:
        file_flag_index = argv_to_parse.index("-f")
        if file_flag_index + 1 < argv_length:
            parsed_file_name = argv_to_parse[file_flag_index + 1]

    if "-d" in argv_to_parse:
        index = argv_to_parse.index("-d") + 1
        while index < argv_length and not argv_to_parse[index].startswith("-"):
            d_args.append(argv_to_parse[index])
            index += 1

    return parsed_file_name, d_args


def get_stdin_input() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_stdin_input_to_file(
        file_path: str,
        input_lines: list[str]
) -> None:
    page_number = 1
    with open(file_path, "a") as source_file:
        source_file.write(
            datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ) + "\n"
        )
        for line in input_lines:
            source_file.write(f"{page_number} {line}\n")
            page_number += 1
        source_file.write("\n")


if __name__ == "__main__":
    args_list = sys.argv[1:]
    file_name, dirs_list = parse_args(args_list)

    path = file_name or ""

    if dirs_list:
        os.makedirs(create_path(dirs_list), exist_ok=True)
        if not file_name:
            sys.exit(0)
        path = create_path([*dirs_list, file_name])

    if path:
        content_lines = get_stdin_input()
        write_stdin_input_to_file(path, content_lines)
