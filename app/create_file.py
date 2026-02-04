# write your code here
import os
import sys
from datetime import datetime


def read_content() -> list[str]:
    """Read lines from terminal until 'stop' is entered."""
    lines: list[str] = []
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1

    return lines


def main() -> None:
    args = sys.argv[1:]

    dir_parts: list[str] = []
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
            file_name = args[i]
            i += 1
        else:
            i += 1

    base_path = os.getcwd()

    if dir_parts:
        base_path = os.path.join(base_path, *dir_parts)
        os.makedirs(base_path, exist_ok=True)

    if not file_name:
        print("Error: file name is required (-f)")
        return

    file_path = os.path.join(base_path, file_name)

    content_lines = read_content()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
