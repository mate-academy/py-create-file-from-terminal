import os
import sys
from datetime import datetime
from typing import List


def create_file(directory: str, filename: str, content: List[str]) -> None:
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, filename), "a") as file:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{formatted_time}\n")
        for i, line in enumerate(content, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    directory = "."
    filename = None
    content = []

    args = iter(sys.argv[1:])
    for arg in args:
        if arg == "-d":
            directory_parts = []
            while True:
                try:
                    part = next(args)
                    if part == "-f":
                        filename = next(args)
                        break
                    directory_parts.append(part)
                except StopIteration:
                    break
            directory = os.path.join(directory, *directory_parts)
        elif arg == "-f" and filename is None:
            filename = next(args)

    if filename is None:
        filename = input("Enter file name: ")

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
