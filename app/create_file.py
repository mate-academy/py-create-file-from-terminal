from datetime import datetime
from pathlib import Path
from typing import List
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dirs", nargs="+", help="List of directories to create"
    )
    parser.add_argument("-f", "--file", help="File name to create")
    args = parser.parse_args()
    if not args.dirs and not args.file:
        parser.error("You must provide -d or -f")
    return args


def create_directories(dirs: List[str]) -> str:
    if not dirs:
        return ""
    path = Path(*dirs)
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def create_file(file_name: str, base_path: str = "") -> str:
    full_path = Path(base_path) / file_name
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.touch(exist_ok=True)
    return str(full_path)


def collect_content() -> List[str]:
    lines: List[str] = []
    while True:
        line = input("Enter content line:")
        if line.strip() == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path: str, lines: List[str]) -> None:
    path = Path(file_path)

    need_newline = False
    if path.exists() and path.stat().st_size > 0:
        with path.open("rb") as f:
            f.seek(-1, 2)
            last_char = f.read(1)
            if last_char != b"\n":
                need_newline = True

    with path.open("a", encoding="utf-8") as f:
        if need_newline:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for idx, line in enumerate(lines, start=1):
            f.write(f"{idx} {line}\n")


def main() -> None:
    args = parse_args()
    base_path = ""
    if args.dirs:
        base_path = create_directories(args.dirs)
    if args.file:
        file_path = create_file(args.file, base_path)
        content = collect_content()
        write_content(file_path, content)
        print(f"Content saved to {file_path}")


if __name__ == "__main__":
    main()
