import os
import sys
from datetime import datetime
from typing import List


def create_file(directory: List[str], filename: str,
                content: List[str]) -> None:
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        filename = os.path.join(directory_path, filename)

    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing_content = f.read()
    else:
        existing_content = ""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = f"{timestamp}\n"
    content_with_timestamp += existing_content.strip() + "\n\n" \
        if existing_content else ""

    line_number = 1
    for line in content:
        if line == "stop":
            break
        content_with_timestamp += f"{line_number} {line}\n"
        line_number += 1

    with open(filename, "w") as f:
        f.write(content_with_timestamp)


def parse_arguments() -> tuple:
    directory: List[str] = []
    filename: str = ""
    content: List[str] = []

    flag = None
    for arg in sys.argv[1:]:
        if arg == "-d":
            flag = "-d"
        elif arg == "-f":
            flag = "-f"
        elif flag == "-d":
            directory.append(arg)
        elif flag == "-f":
            filename = arg
            flag = None
        else:
            content.append(arg)

    if not filename:
        print("Please provide a filename using -f flag")
        sys.exit(1)

    if not content and flag == "-f":
        print("No content provided")
        sys.exit(1)

    return directory, filename, content


def main() -> None:
    directory, filename, content = parse_arguments()
    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
