import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str]:
    directories: list[str] = []
    file_name = ""
    index = 0

    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1
            while index < len(arguments) and arguments[index] not in {
                "-f",
                "-d",
            }:
                directories.append(arguments[index])
                index += 1
        elif arguments[index] == "-f":
            index += 1
            if (
                index < len(arguments)
                and arguments[index] not in {"-d", "-f"}
            ):
                file_name = arguments[index]
                index += 1
        else:
            index += 1

    return directories, file_name


def collect_lines() -> list[str]:
    content_lines: list[str] = []

    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        content_lines.append(user_input)

    return content_lines


def write_content(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{number} {line}"
        for number, line in enumerate(content_lines, start=1)
    ]
    entry = "\n".join([timestamp, *numbered_lines])

    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as source_file:
            if os.path.getsize(file_path) > 0:
                source_file.write("\n")
            source_file.write(entry)
            source_file.write("\n")
    else:
        with open(file_path, "w", encoding="utf-8") as source_file:
            source_file.write(entry)
            source_file.write("\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if file_name:
        file_path = (
            os.path.join(directory_path, file_name)
            if directory_path
            else file_name
        )
        if os.path.dirname(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        content_lines = collect_lines()
        write_content(file_path, content_lines)


if __name__ in {"__main__", "<run_path>"}:
    main()
