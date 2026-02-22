import argparse
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    parser = argparse.ArgumentParser(
        description="Create directories and files with content."
    )

    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        help="Directory path parts",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="File name",
    )

    args = parser.parse_args()

    return args.directories or [], args.file


def create_directory(path_parts: list[str]) -> str:
    if not path_parts:
        return ""

    path = os.path.join(*path_parts)

    os.makedirs(path, exist_ok=True)

    return path


def get_content() -> list[str]:
    lines: list[str] = []

    counter = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(f"{counter} {line}")

        counter += 1

    return lines


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_file(
    directory: str,
    filename: str,
    lines: list[str],
) -> None:

    filepath = filename

    if directory:
        filepath = os.path.join(directory, filename)

    file_exists = os.path.exists(filepath)

    with open(filepath, "a", encoding="utf-8") as file:

        if file_exists:
            file.write("\n")

        file.write(get_timestamp() + "\n")

        for line in lines:
            file.write(line + "\n")


def main() -> None:
    directories, filename = parse_arguments()

    if not filename and not directories:
        print("You must provide -d and/or -f")
        raise SystemExit(1)

    directory_path = create_directory(directories)

    if filename:
        lines = get_content()

        write_file(directory_path, filename, lines)


if __name__ == "__main__":
    main()
