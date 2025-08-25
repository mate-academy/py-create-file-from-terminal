import sys
import os
from datetime import datetime


def parse_args(args):
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        try:
            next_flag = args.index("-f", d_index + 1)
            dir_parts = args[d_index + 1: next_flag]
        except ValueError:
            dir_parts = args[d_index + 1:]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dir_path, file_name


def collect_input():
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":  # case-sensitive
            break
        lines.append(line)
    return lines


def write_block(full_path, lines):
    mode = "a" if os.path.exists(full_path) else "w"
    with open(full_path, mode, encoding="utf-8") as f:
        # if appending to a non-empty file, add blank line first
        if os.path.getsize(full_path) > 0:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def main():
    args = sys.argv[1:]
    dir_path, file_name = parse_args(args)

    if file_name:
        full_path = os.path.join(dir_path, file_name) if dir_path else file_name
        lines = collect_input()
        if lines:
            write_block(full_path, lines)


if __name__ == "__main__":
    main()
