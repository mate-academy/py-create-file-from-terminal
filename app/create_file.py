import os
import sys
from datetime import datetime as dt
from typing import Any



def run() -> None:
    """
    Receives data from the console, handles errors,
    and passes the data to the appropriate functions.
    """
    parsed_data = read_console()

    if (parsed_data["has_directory_flag"]
       and parsed_data["has_file_flag"]):

        make_directory(parsed_data["directories"])
        content = input_content_lines()
        full_path = os.path.join(parsed_data["directory_path"],
                                 parsed_data["filename"])
        fill_file_with_content(full_path, content)

    elif parsed_data["has_directory_flag"]:
        make_directory(parsed_data["directories"])

    elif parsed_data["has_file_flag"]:
        content = input_content_lines()
        fill_file_with_content(parsed_data["filename"], content)


def read_console() -> dict[str, Any]:
    """
    Takes input from the terminal and splits it.
    """
    args = sys.argv[1:]

    result = {
        "has_directory_flag": False,
        "has_file_flag": False,
        "directories": [],
        "filename": "",
        "directory_path": ""
    }

    if not args:
        return result

    i = 0
    while i < len(args):
        if args[i] == "-d":
            result["has_directory_flag"] = True
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                result["directories"].append(args[i])
                i += 1
            result["directory_path"] = os.path.join(*result["directories"])
            continue

        elif args[i] == "-f":
            result["has_file_flag"] = True
            i += 1
            if i < len(args):
                result["filename"] = args[i]
            i += 1

        else:
            i += 1

    return result


def make_directory(directories: list[str]) -> None:
    """
    Creates directory structure from the list of directory names.
    If only -d flag passed, means all items after this flag
    are parts of the path.
    """
    if not directories:
        return

    full_path = os.path.join(*directories)

    os.makedirs(full_path, exist_ok=True)


def input_content_lines() -> list[str]:
    """
    Terminal should ask you to input content lines until user input "stop".
    Returns list of content lines without the "stop" command.
    """
    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

    return content_lines


def fill_file_with_content(filepath: str, content_lines: list[str]) -> None:
    """
    Add timedate (y-m-d h-m-s) to file
    and fill with content from input_content_lines.
    If file exists, appends content with new timestamp.
    """
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(filepath)

    with open(filepath, "a") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")


if __name__ == "__main__":
    run()
