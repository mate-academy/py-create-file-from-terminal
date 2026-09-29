import os
import sys
from datetime import datetime


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

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(content, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    if "-d" in args:
        start = args.index("-d") + 1

        end = len(args)
        for index in range(start, len(args)):
            if args[index].startswith("-"):
                end = index
                break

        directory_parts = args[start:end]

    if "-f" in args:
        file_index = args.index("-f") + 1

        if file_index < len(args):
            file_name = args[file_index]

    directory_path = ""

    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(directory_path, file_name)
        content = get_content()
        write_to_file(file_path, content)


main()
