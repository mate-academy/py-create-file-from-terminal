import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    has_d = "-d" in sys.argv
    has_f = "-f" in sys.argv

    dirs = []
    file_name = None

    if has_d:
        d_index = sys.argv.index("-d")

        if has_f:
            f_index = sys.argv.index("-f")
            dirs = sys.argv[d_index + 1:f_index]
        else:
            dirs = sys.argv[d_index + 1:]

    if has_f:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

    return dirs, file_name


def create_directories(dirs: list[str]) -> str | None:
    if not dirs:
        return None

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_from_user() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    numbered_lines = [
        f"{i} {line}" for i, line in enumerate(lines, start=1)
    ]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [timestamp] + numbered_lines


def write_file_with_content(full_path: str, content: list[str]) -> None:
    file_exists = os.path.exists(full_path)
    file_not_empty = file_exists and os.path.getsize(full_path) > 0

    with open(full_path, "a") as f:
        if file_not_empty:
            f.write("\n")
        f.write("\n".join(content) + "\n")


def main() -> None:
    dirs, file_name = parse_arguments()

    path = create_directories(dirs)

    if not file_name:
        return

    if path:
        full_path = os.path.join(path, file_name)
    else:
        full_path = file_name

    content = get_content_from_user()

    write_file_with_content(full_path, content)


if __name__ == "__main__":
    main()
