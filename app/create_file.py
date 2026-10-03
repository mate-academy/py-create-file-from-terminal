import os
import sys
from datetime import datetime


def get_arguments() -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    arguments = sys.argv[1:]
    index = 0

    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1

            while (
                index < len(arguments)
                and arguments[index] not in ("-d", "-f")
            ):
                directories.append(arguments[index])
                index += 1

        elif arguments[index] == "-f":
            index += 1

            if index < len(arguments):
                file_name = arguments[index]
                index += 1

        else:
            index += 1

    return directories, file_name


def get_content() -> listlines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines

def write_content(file_path: str, lines: list[str]) -> None:
    file_already_has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as file:
        if file_already_has_content:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        for line_number, line in enumerate(lines, start=1):
            file.write(f"{line_number} {line}\n")


def main() -> None:
    directories, file_name = get_arguments()

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if file_name is None:
        return

    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    content = get_content()
    write_content(file_path, content)


main()
