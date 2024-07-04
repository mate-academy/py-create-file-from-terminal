import os
import argparse
from datetime import datetime


def create_file(directory: str, filename: str, content_lines: list) -> None:
    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.writelines(content_lines)
    except OSError as e:
        raise OSError("Error, path isn't correct") from e


def get_content_lines() -> list:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = [timestamp + "\n"]
    idx = 1
    while True:
        line = input("Enter content line (type 'stop' to finish): ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{idx} {line}\n")
        idx += 1
    content_lines.append("\n")
    return content_lines


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content"
    )
    parser.add_argument("-d", "--directory", nargs="+", help="Directory path")
    parser.add_argument("-f", "--file", required=True, help="File name")

    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
    else:
        directory_path = "."

    os.makedirs(directory_path, exist_ok=True)

    if args.file:
        content_lines = get_content_lines()
        create_file(directory_path, args.file, content_lines)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
