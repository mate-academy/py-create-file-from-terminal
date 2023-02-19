import os
import sys
from datetime import datetime
from typing import TextIO


def create_file(filename: str) -> TextIO:
    return open(filename, "a+")


def get_content() -> list[str]:
    content = []
    line = input("Enter content line: ")
    while line != "stop":
        content.append(line)
        line = input("Enter content line: ")
    return content


def write_content(output_file: TextIO, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_file.write(f"\n{timestamp}\n")
    for i, line in enumerate(content):
        output_file.write(f"{i+1} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d") + 1
        filename_index = args.index("-f") + 1
        directory = os.path.join(*args[dir_index:filename_index - 1])
        filename = args[filename_index]
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, filename)
    elif "-d" in args:
        dir_index = args.index("-d") + 1
        directory = os.path.join(*args[dir_index:])
        os.makedirs(directory, exist_ok=True)
        return
    elif "-f" in args:
        filename_index = args.index("-f") + 1
        filename = args[filename_index]
        file_path = filename
    else:
        print("Please specify a filename with the -f flag"
              " or a directory path with the -d flag.")
        return

    if os.path.isfile(file_path):
        output_file = create_file(file_path)
    else:
        output_file = open(file_path, "w")

    content = get_content()
    write_content(output_file, content)
    output_file.close()


if __name__ == "__main__":
    main()
