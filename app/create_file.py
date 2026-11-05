import os
import sys
from datetime import datetime


def parse_arguments(
    args: list[str],
) -> tuple[list[str], str | None]:
    dir_parts: list[str] = []
    file_name: str | None = None

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index < f_index:
            dir_parts = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            file_name = args[f_index + 1]
            dir_parts = args[d_index + 1:]
    elif "-d" in args:
        d_index = args.index("-d")
        dir_parts = args[d_index + 1:]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dir_parts, file_name


def create_directory(dir_parts: list[str]) -> None:
    if dir_parts:
        os.makedirs(os.path.join(*dir_parts), exist_ok=True)


def get_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(path_to_file: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    is_existing_file = (
        os.path.exists(path_to_file) and os.path.getsize(path_to_file) > 0
    )

    with open(path_to_file, "a") as file:
        if is_existing_file:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for index, content in enumerate(lines, start=1):
            file.write(f"{index} {content}\n")


def create_file() -> None:
    dir_parts, file_name = parse_arguments(sys.argv[1:])
    create_directory(dir_parts)

    if file_name:
        path_to_file = (
            os.path.join(*dir_parts, file_name) if dir_parts else file_name
        )
        write_to_file(path_to_file, get_content_lines())


if __name__ in {"__main__", "<run_path>"}:
    create_file()
