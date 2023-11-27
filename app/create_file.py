import sys
import os
from typing import List
import datetime


def create_directories(directory_parts: List[str]) -> str:
    directory = os.path.join(*directory_parts)
    os.makedirs(directory, exist_ok=True)
    return directory


def get_file_content() -> List[str]:
    file_content = []
    print("Enter content lines. Type 'stop' to finish:")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content.append(line)
    return file_content


def append_content_to_file(filepath: str, file_content: List[str]) -> None:
    with open(filepath, "a", encoding="utf-8") as f:
        if os.path.getsize(filepath) == 0:
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        else:
            f.write("\n"
                    + datetime.
                    datetime.
                    now().
                    strftime("%Y-%m-%d %H:%M:%S\n"))
        for index, line in enumerate(file_content, start=1):
            f.write(f"{index} {line}\n")


def main(args: List[str]) -> None:
    directory = None
    filename = None
    i = 1

    while i < len(args):
        if args[i] == "-d":
            i += 1
            directory_parts = []
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
            directory = create_directories(directory_parts)

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
            i += 1

        else:
            i += 1

    if filename:
        filepath = filename
        if directory:
            filepath = os.path.join(directory, filename)

        file_content = get_file_content()
        append_content_to_file(filepath, file_content)


if __name__ == "__main__":
    main(sys.argv)
