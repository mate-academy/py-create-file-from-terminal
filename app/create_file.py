"""Module for creating files and directories from terminal commands."""

import sys
import os
from datetime import datetime


def command_exe() -> None:
    """
    Parse command line arguments and execute file/directory creation.
    """
    term = 1
    path_dir = []
    archive_file = ""
    with_file = False
    with_dir = False

    while term < len(sys.argv):
        if sys.argv[term] == "-d":
            term += 1
            with_dir = True

            while term < len(sys.argv) and sys.argv[term] not in ("-f", "-d"):
                path_dir.append(sys.argv[term])
                term += 1
        elif sys.argv[term] == "-f":
            term += 1
            with_file = True
            if term < len(sys.argv):
                archive_file = sys.argv[term]
                term += 1
        else:
            print(f"Unknown argument: {sys.argv[term]}")
            term += 1

    dir_file = path_creater(path_dir, archive_file, with_file, with_dir)
    if dir_file.endswith(".txt"):
        file_creater(dir_file)


def path_creater(
    path_dir: list,
    archive_file: str,
    is_file: bool = True,
    is_dir: bool = False
) -> str:
    """
    Create and return the file or directory path.

    Args:
        path_dir (list): List of directory names to create.
        archive_file (str): Name of the file to create.
        is_file (bool): Flag indicating whether to create a file.
        is_dir (bool): Flag indicating whether to create directories.

    Returns:
        str: The full path of the created file or directory.
    """
    file_path = os.path.join(*path_dir) if path_dir else ""

    if is_dir and file_path and not os.path.isdir(file_path):
        os.makedirs(file_path, exist_ok=True)
    if is_file and not archive_file.endswith(".txt"):
        archive_file += ".txt"
    return os.path.join(file_path, archive_file) if is_file else file_path


def file_creater(path_file: str) -> None:
    """
    Create a file and write user input to it until "stop" is entered.

    Args:
        path_file (str): The path of the file to create and write to.
    """
    need_newline = os.path.exists(path_file) and os.path.getsize(path_file) > 0

    line_count = 0
    with open(path_file, "a", encoding="utf-8") as f:
        if need_newline:
            f.write("\n")

        actual_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(actual_date + "\n")

        while True:
            line_count += 1
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            f.write(f"{line_count} {line_content}\n")


if __name__ in ("__main__", "<run_path>"):
    command_exe()
