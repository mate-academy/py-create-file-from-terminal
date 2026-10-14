import argparse
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", default=[])
    parser.add_argument("-f", default=None)

    known_args, _ = parser.parse_known_args()
    return known_args.d, known_args.f


def create_directories(directories: list[str]) -> str:
    target_dir = os.path.join(*directories) if directories else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
    return target_dir


def collect_content() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]

    idx = 1
    while True:
        try:
            line = input("Enter content line: ")
        except (EOFError, KeyboardInterrupt):
            break
        if line == "stop":
            break
        formatted_lines.append(f"{idx} {line}")
        idx += 1

    return "\n".join(formatted_lines) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    is_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8") as f:
        if is_not_empty:
            f.write("\n")
        f.write(content)


def main() -> None:
    directories, file_name = parse_arguments()
    target_dir = create_directories(directories)

    if not file_name:
        return

    if target_dir:
        file_path = os.path.join(target_dir, file_name)
    else:
        file_path = file_name

    new_content = collect_content()
    write_to_file(file_path, new_content)


main()
