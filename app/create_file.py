import sys
import os
from datetime import datetime
from typing import List


def create_directories(dirs: List[str]) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def get_file_content() -> List[str]:
    lines: List[str] = []

    while True:
        line = input("Enter content line: ")

        if line.lower() == "stop":
            break

        lines.append(line)

    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted: List[str] = [timestamp]

    for i, line in enumerate(lines, start=1):
        formatted.append(f"{i} {line}")

    return "\n".join(formatted)


def write_to_file(file_path: str, content: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n\n")

        f.write(content)


def main() -> None:
    args = sys.argv[1:]

    dir_parts: List[str] = []
    file_name: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    base_path = ""

    if dir_parts:
        base_path = create_directories(dir_parts)

    if file_name:
        if base_path:
            file_path = os.path.join(base_path, file_name)
        else:
            file_path = file_name

        lines = get_file_content()
        content = format_content(lines)
        write_to_file(file_path, content)

        print(f"File created at: {file_path}")


if __name__ == "__main__":
    main()
