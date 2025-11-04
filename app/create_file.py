import os
import datetime
import argparse
from typing import Any


def content_input() -> list:
    """
    Collect timestamped multiline user input.

    Returns:
        list: First element is a timestamp.
              Following elements are numbered lines entered by the user
              (input ends when the user types 'stop').
    """

    content = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.append(timestamp)

    print("Enter file content line by line (type 'stop' to finish):")
    lines = []
    while True:
        line = input("Line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    for idx, text in enumerate(lines, start=1):
        content.append(f"{idx} {text}")

    return content


def parse_args() -> Any:
    """
    Parse command-line arguments using argparse.

    Flags:
        -d  One or more directory names
        -f  File name

    Returns:
        argparse.Namespace: parsed args with .dirs and .file
    """
    parser = argparse.ArgumentParser(description="Create dirs and file.")

    parser.add_argument(
        "-d", "--dirs",
        nargs="+",
        help="Directories to create"
    )

    parser.add_argument(
        "-f", "--file",
        required=True,
        help="File name to create or append to"
    )

    return parser.parse_args()


def create_directories(dirs: list) -> str:
    """
    Create directory chain if provided.

    Args:
        dirs (list): list of directories

    Returns:
        str: full directory path or empty string
    """
    if dirs:
        full_path = os.path.join(*dirs)
        os.makedirs(full_path, exist_ok=True)
        return full_path

    return ""


def write_file(dir_path: str, file_name: str) -> None:
    """
    Create or append to file and write timestamp+content.

    Args:
        dir_path (str): directory path
        file_name (str): target file name
    """
    file_path = os.path.join(dir_path, file_name)

    data = content_input()
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")
        for line in data:
            f.write(line + "\n")


def create_file() -> None:
    args = parse_args()

    dir_path = create_directories(args.dirs)
    write_file(dir_path, args.file)
