import os
import sys
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
            continue
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                file_name = args[i]
                i += 1
            continue
        i += 1

    return directories, file_name


def read_content_lines() -> list[str]:
    lines = []
    while True:
        try:
            line = input("Enter content line: ")
        except (EOFError, KeyboardInterrupt):
            break
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [f"{timestamp}"]
    for idx, line in enumerate(lines, start=1):
        formatted_lines.append(f"{idx} {line}")
    return "\n".join(formatted_lines) + "\n"


def main() -> None:
    directories, file_name = parse_arguments()

    target_dir = os.path.join(*directories) if directories else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        file_path = (
            os.path.join(target_dir, file_name) if target_dir else file_name
        )

        lines = read_content_lines()
        new_content = format_content(lines)

        mode = "a" if os.path.exists(file_path) else "w"
        with open(file_path, mode, encoding="utf-8") as f:
            if mode == "a" and os.path.getsize(file_path) > 0:
                f.write("\n")
            f.write(new_content)


if __name__ == "__main__":
    main()
