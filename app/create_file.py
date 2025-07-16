import os
import sys
from datetime import datetime as dt
from typing import Any


def get_arguments() -> dict[str, Any]:
    args = sys.argv[1:]

    result = {
        "has_directory_flag": False,
        "has_file_flag": False,
        "filename": "",
        "directory_path": ""
    }

    if not args:
        return result

    directories = []
    i = 0

    while i < len(args):
        if args[i] == "-d":
            result["has_directory_flag"] = True
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
            result["directory_path"] = os.path.join(*directories)
            continue

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                result["has_file_flag"] = True
                result["filename"] = args[i]
            i += 1

        else:
            i += 1

    return result


def fill_file_with_content(filepath: str) -> None:
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    has_content = os.path.exists(filepath) and os.path.getsize(filepath) > 0

    with open(filepath, "a") as file:
        if has_content:
            file.write("\n")

        file.write(f"{timestamp}\n")

        i = 1
        while True:
            line = input("Enter content line: ")

            if line.lower() == "stop":
                break

            file.write(f"{i} {line}\n")
            i += 1


def run() -> None:
    parsed_data = get_arguments()
    has_dir_flag = parsed_data["has_directory_flag"]
    has_file_flag = parsed_data["has_file_flag"]

    if has_dir_flag:
        if parsed_data["directory_path"]:
            os.makedirs(parsed_data["directory_path"], exist_ok=True)

    if has_file_flag:
        full_path = os.path.join(
            parsed_data["directory_path"],
            parsed_data["filename"]
        )
        fill_file_with_content(str(full_path))

    if not (has_dir_flag or has_file_flag):
        print("No -d or -f flags were given")


if __name__ == "__main__":
    run()
