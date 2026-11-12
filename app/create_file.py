import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dirs = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if d_index < f_index:
                dirs = args[d_index + 1 : f_index]
            else:
                dirs = args[d_index + 1 :]
        else:
            dirs = args[d_index + 1 :]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    return dirs, filename


def create_directories(dirs: list[str]) -> str:
    if not dirs:
        return ""
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def collect_content_lines() -> list[str]:
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)
    return lines


def write_content_to_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")


def main() -> None:
    dirs, filename = parse_args(sys.argv[1:])
    dir_path = create_directories(dirs)

    if filename:
        file_path = os.path.join(dir_path, filename) if dir_path else filename
        lines = collect_content_lines()
        write_content_to_file(file_path, lines)


if __name__ in ("__main__", "<run_path>"):
    main()
