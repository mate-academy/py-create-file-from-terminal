import os
import sys
from datetime import datetime


def get_arguments() -> tuple[list[str], str | None]:
    arguments = sys.argv[1:]

    directories = []
    file_name = None

    if "-d" in arguments:
        d_index = arguments.index("-d")
        directories = arguments[d_index + 1:]

        if "-f" in directories:
            f_index = directories.index("-f")
            directories = directories[:f_index]

    if "-f" in arguments:
        f_index = arguments.index("-f")

        if f_index + 1 < len(arguments):
            file_name = arguments[f_index + 1]

    return directories, file_name


def create_directory(directories: list[str]) -> str:
    if not directories:
        return ""

    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

    return path


def get_content() -> list[str]:
    content = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(line)

    return content


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for line_number, line in enumerate(content, start=1):
            file.write(f"{line_number} {line}\n")


def main() -> None:
    directories, file_name = get_arguments()

    directory_path = create_directory(directories)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)

    content = get_content()
    write_to_file(file_path, content)


main()
