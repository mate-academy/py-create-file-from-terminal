import os
import argparse
from datetime import datetime


def get_user_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as target_file:
        if mode == "a":
            target_file.write("\n")

        target_file.write(f"{timestamp}\n")
        for line_number, content in enumerate(lines, 1):
            target_file.write(f"{line_number} {content}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create/update files with numbered lines."
    )
    parser.add_argument("-d", "--dir", nargs="+", help="Directory path parts")
    parser.add_argument("-f", "--file", required=True, help="Filename")

    args = parser.parse_args()

    target_path = os.path.join(*args.dir) if args.dir else "."
    if args.dir:
        os.makedirs(target_path, exist_ok=True)

    full_file_path = os.path.join(target_path, args.file)
    content_lines = get_user_lines()

    write_to_file(full_file_path, content_lines)


if __name__ == "__main__":
    main()
