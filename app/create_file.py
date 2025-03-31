import os
import argparse
from datetime import datetime
from typing import List


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a file with content from terminal."
    )
    parser.add_argument(
        "-d", "--directory",
        nargs="*",
        default=[],
        help="Directory path parts (e.g., dir1 dir2)"
    )
    parser.add_argument(
        "-f", "--file",
        required=True,
        help="File name (e.g., file.txt)"
    )
    return parser.parse_args()


def create_directory(path_parts: List[str]) -> str:
    if not path_parts:
        return os.getcwd()
    full_path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def get_user_content() -> List[str]:
    print("Enter content lines (type 'stop' to finish):")
    lines = []
    while True:
        line = input("Enter content line: ").strip()
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> List[str]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp] + [f"{i + 1} {line}" for i, line in enumerate(lines)]


def write_to_file(file_path: str, content: List[str]) -> None:
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        content = [""] + content
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")


def main() -> None:
    args = parse_arguments()
    full_path = create_directory(args.directory)
    file_path = os.path.join(full_path, args.file)
    user_lines = get_user_content()
    formatted_content = format_content(user_lines)
    write_to_file(file_path, formatted_content)
    print(f"File '{args.file}' created or updated at '{file_path}'.")


if __name__ == "__main__":
    main()
