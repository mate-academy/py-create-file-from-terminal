import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    dirs = []
    filename = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1
    return dirs, filename


def main() -> None:
    dirs, filename = parse_arguments(sys.argv[1:])

    target_dir = os.path.join(*dirs) if dirs else ""

    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if not filename:
        return

    file_path = os.path.join(target_dir, filename) if target_dir else filename

    file_exists = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_parts = [timestamp]
    for idx, line in enumerate(lines, start=1):
        content_parts.append(f"{idx} {line}")

    new_content = "\n".join(content_parts) + "\n"

    if file_exists:
        new_content = "\n" + new_content

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(new_content)


main()
