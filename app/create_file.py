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


def create_directory_and_file(args: list[str]) -> str:
    dir_index = args.index("-d") + 1
    filename_index = args.index("-f") + 1
    directory = os.path.join(*args[dir_index:filename_index - 1])
    filename = args[filename_index]
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    return file_path


def get_output_file(file_path: str) -> TextIO:
    if os.path.isfile(file_path):
        return create_file(file_path)
    else:
        return open(file_path, "w")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        file_path = create_directory_and_file(args)
    elif "-d" in args:
        directory = os.path.join(*args[args.index("-d") + 1:])
        os.makedirs(directory, exist_ok=True)
        return
    elif "-f" in args:
        file_path = args[args.index("-f") + 1]
    else:
        print("Please specify a filename with the -f flag"
              " or a directory path with the -d flag.")
        return

    with get_output_file(file_path) as output_file:
        content = get_content()
        write_content(output_file, content)


if __name__ == "__main__":
    main()
