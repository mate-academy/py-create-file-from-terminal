import sys
import os
from datetime import datetime


def collect_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_content(filepath: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  -d dir1 dir2 ...   to create directories")
        print("  -f filename        to create/write file")
        print("  -d ... -f file.txt to create directory + file")

        return

    dir_path = ""
    filename = ""

    if "-d" in args:
        d_index = args.index("-d") + 1
        directories = []

        for item in args[d_index:]:
            if item.startswith("-"):
                break
            directories.append(item)

        if directories:
            dir_path = os.path.join(*directories)
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index >= len(args):
            print("Error: filename is missing after -f")

            return

        filename = args[f_index]

    if filename:
        filepath = os.path.join(dir_path, filename) if dir_path else filename
        lines = collect_content()
        write_content(filepath, lines)


if __name__ == "__main__":
    main()
