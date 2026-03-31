import sys
import os
import datetime
from typing import List, Tuple, Optional


def get_args() -> Tuple[List[str], Optional[str]]:
    args: List[str] = sys.argv[1:]

    dirs: List[str] = []
    file_name: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ["-d", "-f"]:
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return dirs, file_name


def create_dirs(dirs: List[str]) -> str:
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def get_content() -> List[str]:
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> str:
    timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result: List[str] = [timestamp]

    for i, line in enumerate(lines, start=1):
        result.append(f"{i} {line}")

    return "\n".join(result) + "\n"


def write_file(path: str, file_name: str, content: str) -> None:
    full_path: str = os.path.join(path, file_name) if path else file_name
    file_exists: bool = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")  # відступ між блоками
        output_file.write(content)


def main() -> None:
    dirs, file_name = get_args()

    path: str = create_dirs(dirs)

    if file_name:
        lines: List[str] = get_content()
        content: str = format_content(lines)
        write_file(path, file_name, content)


if __name__ == "__main__":
    main()
