import sys
import os
from datetime import datetime


def parse_args(argv):
    directories = []
    filename = None
    i = 0
    while i < len(argv):
        if argv[i] == "-d":
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                directories.append(argv[i])
                i += 1
        elif argv[i] == "-f":
            i += 1
            if i < len(argv):
                filename = argv[i]
                i += 1
            else:
                raise ValueError("Missing filename after -f")
        else:
            i += 1
    return directories, filename


def create_dirs(dirs):
    if not dirs:
        return os.path.abspath(os.getcwd())
    else:
        path = os.path.join(os.getcwd(), *dirs)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)


def read_content():
    lines = []
    while True:
        s = input("Enter content line: ")
        if s == "stop":
            break
        lines.append(s)
    return lines


def append_to_file(path, lines):
    need_sep = os.path.exists(path) and os.path.getsize(path) > 0
    with open(path, "a", encoding="utf-8") as f:
        if need_sep:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def main():
    dirs, filename = parse_args(sys.argv[1:])
    target = create_dirs(dirs)

    if dirs and filename is None:
        return

    if filename is None:
        filename = input("Enter filename: ")


    if not filename.strip():
        print("Empty filename")
        return

    full_path = os.path.join(target, filename)
    lines = read_content()
    append_to_file(full_path, lines)
    print(f"File saved to {full_path}")


if __name__ == "__main__":
    main()
