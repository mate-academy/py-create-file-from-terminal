from datetime import datetime
import sys
import os
from typing import List, Tuple, Optional


def parse_arguments(argv: List[str]) -> Tuple[List[str], Optional[str]]:
    dir_parts: List[str] = []
    file_name: Optional[str] = None
    index: int = 0

    while index < len(argv):
        if argv[index] == "-d":
            index += 1
            while index < len(argv) and not argv[index].startswith("-"):
                dir_parts.append(argv[index])
                index += 1
        elif argv[index] == "-f":
            index += 1
            if index < len(argv):
                file_name = argv[index]
                index += 1
        else:
            index += 1

    return dir_parts, file_name


def ensure_directories(dir_parts: List[str]) -> str:
    if not dir_parts:
        return ""
    dir_path: str = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def collect_input_lines() -> List[str]:
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def append_timestamped_block(file_path: str, lines: List[str]) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    needs_leading_newline: bool = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as out_file:
        if needs_leading_newline:
            out_file.write(f"\n{timestamp}\n")
        else:
            out_file.write(f"{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            out_file.write(f"{i} {line}\n")


def main() -> None:
    args: List[str] = sys.argv[1:]
    if not args:
        return

    dir_parts, file_name = parse_arguments(args)
    dir_path: str = ensure_directories(dir_parts)

    if file_name:
        file_path: str = os.path.join(dir_path, file_name)\
            if dir_path else file_name
        lines: List[str] = collect_input_lines()
        append_timestamped_block(file_path, lines)


if __name__ == "__main__":
    main()
