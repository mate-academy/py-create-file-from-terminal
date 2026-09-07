
import os
import sys
from datetime import datetime


def get_arguments() -> tuple[list[str], str | None]:
    directories = []
    file_name = None

    i = 1

    while i < len(sys.argv):
        argument = sys.argv[i]

        if argument == "-d":
            i += 1

            while i < len(sys.argv) and sys.argv[i] not in ("-d", "-f"):
                directories.append(sys.argv[i])
                i += 1

            continue

        if argument == "-f":
            i += 1

            if i < len(sys.argv):
                file_name = sys.argv[i]

        i += 1

    return directories, file_name


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def create_directories(directories: list[str]) -> str:
    if not directories:
        return ""

    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path


def create_file(
    directory_path: str,
    file_name: str,
    lines: list[str],
) -> None:
    file_path = os.path.join(directory_path, file_name)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    directories, file_name = get_arguments()
    directory_path = create_directories(directories)

    if file_name:
        lines = get_content()
        create_file(directory_path, file_name, lines)


main()
