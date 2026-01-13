import os
import sys
from datetime import datetime


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:
    dir_parts: list[str] = []
    file_name: str | None = None

    if "-d" in argv:
        d_index = argv.index("-d")
        i = d_index + 1
        while i < len(argv) and not argv[i].startswith("-"):
            dir_parts.append(argv[i])
            i += 1

    if "-f" in argv:
        f_index = argv.index("-f")
        if f_index + 1 >= len(argv):
            print("Error: -f flag requires file name")
            sys.exit(1)
        file_name = argv[f_index + 1]

    return dir_parts, file_name


def read_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_block(file_path: str, lines: list[str]) -> None:
    file_exists = os.path.exists(file_path)
    has_content = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as f:
        if has_content:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            f.write(f"{index} {line}\n")


def main() -> None:
    argv = sys.argv[1:]

    if not argv:
        print("Usage:")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    dir_parts, file_name = parse_args(argv)

    if not dir_parts and file_name is None:
        print("Usage:")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    if dir_parts:
        target_dir = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(target_dir, exist_ok=True)
    else:
        target_dir = os.getcwd()

    if file_name is None:
        if dir_parts:
            print(f"Directory created (or already existed): {target_dir}")
            return

    file_path = os.path.join(target_dir, file_name)

    lines = read_content_lines()

    write_block(file_path, lines)

    print(f"File updated: {file_path}")


if __name__ == "__main__":
    main()
