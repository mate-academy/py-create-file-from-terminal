import os
import sys
from datetime import datetime


def create_directory(path_parts: list[str]) -> str:
    directory = os.path.join(*path_parts)
    os.makedirs(directory, exist_ok=True)
    return directory


def create_file(file_name: str, content: str) -> None:
    with open(file_name, "a") as file:
        file.write(content)


def get_timestamp() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py "
              "[-d directory_path] [-f file_name]")
        sys.exit(1)

    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory_path = sys.argv[directory_index:]
        directory = create_directory(directory_path)
    else:
        directory = os.getcwd()

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = os.path.join(directory, sys.argv[file_index])
        content = ""

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content += line + "\n"

        timestamp = get_timestamp()
        content_with_timestamp = f"{timestamp}\n{content}"

        if os.path.exists(file_name):
            content_with_numbering = add_line_numbers(content_with_timestamp)
            create_file(file_name, content_with_numbering)
        else:
            create_file(file_name, content_with_timestamp)


def add_line_numbers(content: str) -> str:
    lines = content.split("\n")
    numbered_lines = [f"{i} {line}" for i, line in enumerate(lines, start=1)]
    return "\n".join(numbered_lines)


main()
