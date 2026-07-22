import sys
import os
from datetime import datetime


def parse_args() -> tuple[list[str] | None, str | None]:
    argv = sys.argv[1:]
    dirs: list[str] | None = None
    file_name: str | None = None

    if "-d" in argv:
        d_index = argv.index("-d")
        dirs = []
        for item in argv[d_index + 1:]:
            if item == "-f":
                break
            dirs.append(item)

    if "-f" in argv:
        f_index = argv.index("-f")
        if f_index + 1 < len(argv):
            file_name = argv[f_index + 1]

    return dirs, file_name


def read_content_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path: str, lines: list[str]) -> None:
    file_exists_with_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block_lines = [timestamp]
    for i, line in enumerate(lines, start=1):
        block_lines.append(f"{i} {line}")
    block = "\n".join(block_lines) + "\n"

    with open(file_path, "a") as f:
        if file_exists_with_content:
            f.write("\n")
        f.write(block)


def main() -> None:
    dirs, file_name = parse_args()

    if not dirs and not file_name:
        print("Error: you must pass -d, -f, or both.")
        return

    dir_path = None
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory created: {dir_path}")

    if file_name:
        file_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )
        lines = read_content_lines()
        write_content(file_path, lines)
        print(f"File created/updated: {file_path}")


main()
