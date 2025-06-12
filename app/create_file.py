import sys
import os
from datetime import datetime
from typing import List


def get_input_lines() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = [timestamp]
    formatted += [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return "\n".join(formatted) + "\n"


def main() -> None:
    args = sys.argv[1:]
    dir_parts = []
    filename = None

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
                filename = args[i]
            i += 1
        else:
            i += 1

    base_path = os.getcwd()
    if dir_parts:
        base_path = os.path.join(base_path, *dir_parts)
        os.makedirs(base_path, exist_ok=True)

    if filename:
        file_path = os.path.join(base_path, filename)
        lines = get_input_lines()
        content = format_content(lines)

        with open(file_path, "a", encoding="utf-8") as f:
            if os.path.getsize(file_path) > 0:
                f.write("\n")
            f.write(content)


if __name__ == "__main__":
    main()
