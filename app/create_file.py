import sys
import os
from datetime import datetime


def build_dir_path(parts: list[str]) -> str:
    base_path = os.getcwd()
    return os.path.join(base_path, *parts) if parts else base_path


def ensure_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def collect_input(prompt: str = "Enter content line:") -> list[str]:
    lines = []
    while True:
        line = input(f"{prompt} ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def format_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_block(file_path: str, timestamp: str, lines: list[str]) -> None:
    file_exists = os.path.exists(file_path)
    non_empty = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as f:
        if non_empty:
            f.write("\n")

        f.write(f"{timestamp}\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
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
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
            else:
                raise ValueError("Error: -f flag requires a filename")
        else:
            raise ValueError(f"Unknown argument: {args[i]}")
    return dirs, filename


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 ...")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 ... -f filename")
        return

    try:
        dirs, filename = parse_args(args)
    except ValueError as e:
        print(e)
        return

    dir_path = build_dir_path(dirs)
    if dirs:
        ensure_directories(dir_path)
        print(f"Directory created: {dir_path}")

    if filename:
        file_path = os.path.join(dir_path, filename)
        lines = collect_input()
        timestamp = format_timestamp()
        write_block(file_path, timestamp, lines)
        print(f"File created/updated: {file_path}")


if __name__ == "__main__":
    main()
