import sys
import os
from datetime import datetime


def find_next_flag(start_idx: int) -> int:
    for i in range(start_idx + 1, len(sys.argv)):
        if sys.argv[i].startswith("-"):
            return i
    return len(sys.argv)


def parse_arguments() -> tuple[list, str | None]:
    if "-d" in sys.argv and "-f" in sys.argv:
        idx_d = sys.argv.index("-d")
        idx_f = sys.argv.index("-f")

        if idx_d < idx_f:
            dirs = sys.argv[idx_d + 1:idx_f]
            filename = sys.argv[idx_f + 1]
        else:
            next_flag_idx = find_next_flag(idx_d)
            dirs = sys.argv[idx_d + 1:next_flag_idx]
            filename = sys.argv[idx_f + 1]

    elif "-d" in sys.argv:
        dirs = sys.argv[sys.argv.index("-d") + 1:]
        filename = None
    elif "-f" in sys.argv:
        dirs = []
        filename = sys.argv[sys.argv.index("-f") + 1]
    else:
        dirs = []
        filename = sys.argv[-1]

    return dirs, filename


dirs, filename = parse_arguments()


def create_directories(dirs: list) -> str:
    if dirs:
        path = os.path.join(".", *dirs)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


path = create_directories(dirs)


def get_file_content() -> list:
    if filename:
        lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            lines.append(user_input)
        return lines


lines = get_file_content()


def write_to_file(filepath: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as f:
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


filepath = os.path.join(path, filename) if filename else None
if filepath:
    write_to_file(filepath, lines)
