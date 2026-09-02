import os
import sys
from datetime import datetime


def get_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered = [
        f"{idx} {line}"
        for idx, line in enumerate(lines, 1)
    ]
    return "\n".join([timestamp, *numbered]) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a", encoding="utf-8") as f:
        if has_content:
            f.write("\n")
        f.write(content)


def main() -> None:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and args[i] not in ("-d", "-f"):
                file_name = args[i]
                i += 1
        else:
            i += 1

    target_dir = os.path.join(*dir_parts) if dir_parts else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        target_file = (
            os.path.join(target_dir, file_name)
            if target_dir
            else file_name
        )
        lines = get_lines()
        content = format_content(lines)
        write_to_file(target_file, content)


main()
