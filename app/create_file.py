import os
import sys
from datetime import datetime


def parse_arguments(argv: list[str]) -> tuple[list[str], str]:
    directories: list[str] = []
    file_name: str = ""

    has_d = "-d" in argv
    has_f = "-f" in argv

    if not has_d and not has_f:
        raise ValueError("You must pass at least -d or -f")

    d_index = argv.index("-d") if has_d else None
    f_index = argv.index("-f") if has_f else None

    if has_d:
        if has_f and f_index > d_index:
            directories = argv[d_index + 1:f_index]
        else:
            directories = argv[d_index + 1:]

    if has_f:
        if has_d and d_index > f_index:
            remaining = argv[f_index + 1:d_index]
        else:
            remaining = argv[f_index + 1:]
        if remaining:
            file_name = remaining[0]

    return directories, file_name


def read_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def build_content_block(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{index} {line}" for index, line in enumerate(lines, start=1)
    ]
    numbered_text = "\n".join(numbered_lines)
    return f"{timestamp}\n{numbered_text}\n"


def write_file(path: str, lines: list[str]) -> None:
    content_block = build_content_block(lines)
    file_exists = os.path.exists(path)
    mode = "a" if file_exists else "w"

    with open(path, mode, encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(content_block)


def main() -> None:
    argv = sys.argv[1:]
    directories, file_name = parse_arguments(argv)

    dir_path = os.path.join(*directories) if directories else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        lines = read_content_lines()
        full_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )
        write_file(full_path, lines)
        print(f"File '{full_path}' updated successfully.")
    elif dir_path:
        print(f"Directory '{dir_path}' created successfully.")


main()
