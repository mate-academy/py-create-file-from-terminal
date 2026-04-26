import sys
import os
from datetime import datetime
from typing import List


def parse_args(args: List[str]) -> tuple[str | None, str | None]:
    dir_parts: List[str] = []
    file_name: str | None = None

    i = 1
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
            i += 1
            continue

        i += 1

    dir_path = os.path.join(*dir_parts) if dir_parts else None
    return dir_path, file_name


def read_content() -> str:
    lines: List[str] = []
    index = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        lines.append(f"{index} {line}")
        index += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{timestamp}\n" + "\n".join(lines) + "\n"


def ensure_directory(dir_path: str | None) -> None:
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)


def write_to_file(file_path: str, content: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n" + content)
    else:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)


def main() -> None:
    dir_path, file_name = parse_args(sys.argv)

    if file_name is None:
        return

    ensure_directory(dir_path)

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    content = read_content()
    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
