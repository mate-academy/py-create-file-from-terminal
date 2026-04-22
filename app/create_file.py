import os
import sys
from datetime import datetime


def parse_args() -> tuple[list[str], str | None]:
    args = sys.argv

    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        for arg in args[d_index:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)
        if not dirs:
            print("No directories provided after -d.")
            sys.exit(1)

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args) and not args[f_index].startswith("-"):
            file_name = args[f_index]
        else:
            print("No file name provided after -f.")
            sys.exit(1)

    return dirs, file_name


def create_directories(dirs: list[str]) -> str:
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def read_lines_until_stop() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def build_text_block(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    numbered_lines = [
        f"{i + 1} {line}" for i, line in enumerate(lines)
    ]

    return "\n".join([timestamp] + numbered_lines) + "\n"


def write_block(path: str, file_name: str, content: str) -> None:
    full_path = os.path.join(path, file_name) if path else file_name

    mode = "a" if os.path.exists(full_path) else "w"

    with open(full_path, mode) as f:
        if mode == "a":
            f.write("\n")
        f.write(content)


def main() -> None:
    dirs, file_name = parse_args()

    if not dirs and not file_name:
        print("No arguments provided.")
        return

    path = create_directories(dirs)

    if dirs and not file_name:
        print("Directories created.")
        return

    lines = read_lines_until_stop()
    content = build_text_block(lines)

    write_block(path, file_name, content)


main()
