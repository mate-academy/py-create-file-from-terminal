import os
import sys
from datetime import datetime


def parse_arguments(
    arguments: list[str],
) -> tuple[list[str], str | None]:
    directory_parts = []
    file_name = None

    if "-d" in arguments and "-f" in arguments:
        d_index = arguments.index("-d")
        f_index = arguments.index("-f")
        if d_index < f_index:
            directory_parts = arguments[d_index + 1 : f_index]
            file_name = arguments[f_index + 1]
        else:
            file_name = arguments[f_index + 1]
            directory_parts = arguments[d_index + 1 :]
    elif "-d" in arguments:
        d_index = arguments.index("-d")
        directory_parts = arguments[d_index + 1 :]
    elif "-f" in arguments:
        f_index = arguments.index("-f")
        file_name = arguments[f_index + 1]

    return directory_parts, file_name


def collect_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = ""

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r", encoding="utf-8") as existing_file:
            existing_content = existing_file.read()
        if existing_content.endswith("\n"):
            prefix = "\n"
        else:
            prefix = "\n\n"

    with open(file_path, "a", encoding="utf-8") as target_file:
        target_file.write(f"{prefix}{timestamp}\n")
        for line_number, line_content in enumerate(lines, start=1):
            target_file.write(f"{line_number} {line_content}\n")


def main() -> None:
    directory_parts, file_name = parse_arguments(sys.argv[1:])

    directory_path = ""
    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        lines = collect_content()
        write_file(file_path, lines)


if __name__ in ("__main__", "<run_path>"):
    main()
