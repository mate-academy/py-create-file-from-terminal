import sys
import os
from datetime import datetime

def create_file(args, input_lines):
    has_d = "-d" in args
    has_f = "-f" in args

    if has_d:
        idx_d = args.index("-d")
        if has_f:
            idx_f = args.index("-f")
            dirs = args[idx_d + 1: idx_f]
        else:
            dirs = args[idx_d + 1:]
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = None

    if has_f:
        idx_f = args.index("-f")
        filename = args[idx_f + 1]
    else:
        raise ValueError("No file name provided")

    full_path = os.path.join(dir_path, filename) if dir_path else filename

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    need_blank = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a", encoding="utf-8") as f:
        if need_blank:
            f.write("\n")
        f.write(ts + "\n")
        for i, line in enumerate(input_lines, start=1):
            f.write(f"{i} {line}\n")

    return full_path


def main():
    args = sys.argv[1:]
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    create_file(args, lines)


if __name__ == "__main__":
    main()
