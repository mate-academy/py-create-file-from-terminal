import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[str | None, str | None]:
    """
    Parses command-line arguments.
    Supports:
        -d dir1 dir2 ...   → only create directories
        -f filename        → only create file
        -d ... -f file     → create dirs + file inside them

    Returns a tuple: (dir_path, file_name)
    dir_path may be None if -d was not provided
    file_name may be None if -f was not provided
    """
    dir_parts = []
    file_name = None

    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 >= len(args):
            raise Exception("Missing file name after -f")

        next_arg = args[f_index + 1]
        if next_arg.startswith("-"):
            raise Exception("Invalid file name")

        file_name = next_arg

    if "-d" in args:
        d_index = args.index("-d")

        for item in args[d_index + 1:]:
            if item.startswith("-"):
                break
            dir_parts.append(item)

        if not dir_parts:
            raise Exception("No directory names provided after -d")

        dir_path = os.path.join(*dir_parts)
    else:
        dir_path = None

    return dir_path, file_name


def get_full_path(dir_path: str | None, file_name: str | None) -> str | None:
    """
    Creates directories (if provided) and returns full path for the file.
    If only directories are provided and no file, returns None.
    """
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        return os.path.join(dir_path, file_name) if dir_path else file_name

    return None


def content_input() -> list[str]:
    """
    Reads user input lines until 'stop'.
    Adds timestamp and numbering.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]

    print("Enter content line by line (type 'stop' to finish):")

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    for idx, text in enumerate(lines, start=1):
        content.append(f"{idx} {text}")

    return content


def write_file(full_path: str) -> None:
    """
    Writes timestamp + numbered lines into a file.
    If the file exists, adds ONE blank line before writing new content.
    """
    content = content_input()
    file_exists = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")

        for line in content:
            f.write(line + "\n")

    print(f"File created/updated at: {full_path}")


def main() -> None:
    args = sys.argv

    dir_path, file_name = parse_args(args)

    full_path = get_full_path(dir_path, file_name)

    if full_path is None:
        print(f"Directories created at: {dir_path}")
        return

    write_file(full_path)


if __name__ == "__main__":
    main()
