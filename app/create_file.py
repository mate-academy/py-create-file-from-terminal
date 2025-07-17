import os
import sys
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content_to_file(filepath: str, lines: list) -> None:
    with open(filepath, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            f.write(f"{idx} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    dir_path = ""
    filename = ""

    if "-d" in args:
        d_index = args.index("-d")
        # якщо є -f, беремо лише частину між -d і -f
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1:f_index]
        else:
            dir_parts = args[d_index + 1:]
        dir_path = create_path(dir_parts)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            filename = args[f_index + 1]
        except IndexError:
            print("Error: Missing file name after -f flag.")
            return

    if not filename:
        print("No file to write. Exiting.")
        return

    full_path = os.path.join(dir_path, filename) if dir_path else filename
    content_lines = get_content()
    write_content_to_file(full_path, content_lines)
    print(f"Content saved to {full_path}")


if __name__ == "__main__":
    main()
