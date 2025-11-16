import sys
import os
from datetime import datetime


def build_directory_path(directory_list: list[str]) -> str:
    if not directory_list:
        return ""
    return os.path.join(*directory_list)


def collect_content_lines() -> list[str]:
    lines: list[str] = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def append_to_file(filepath: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = collect_content_lines()

    file_exists = os.path.exists(filepath)
    file_not_empty = file_exists and os.path.getsize(filepath) > 0

    with open(filepath, "a", encoding="utf-8") as file:
        if file_not_empty:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for line in content_lines:
            file.write(f"{line}\n")


def parse_arguments(
    arguments: list[str],
) -> tuple[list[str], str | None]:
    directory_parts: list[str] = []
    filename: str | None = None

    i = 0
    while i < len(arguments):
        if arguments[i] == "-d":
            i += 1
            while (
                i < len(arguments)
                and not arguments[i].startswith("-")
            ):
                directory_parts.append(arguments[i])
                i += 1
            continue

        if arguments[i] == "-f":
            i += 1
            if i < len(arguments):
                filename = arguments[i]
                i += 1
            continue

        i += 1

    return directory_parts, filename


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided.")
        return

    directory_parts, filename = parse_arguments(args)
    directory_path = build_directory_path(directory_parts)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if filename:
        filepath = os.path.join(directory_path, filename)
        append_to_file(filepath)
        print(f"File updated: {filepath}")
        return

    print("Nothing to do: -f flag was not provided.")


if __name__ == "__main__":
    main()
