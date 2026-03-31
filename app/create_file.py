import sys
import os
from datetime import datetime


def parse_args(args):
    dirs = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]
        else:
            print("Error: filename not provided")
            sys.exit()

    return dirs, filename


def create_dirs(dirs):
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def get_user_input():
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_file(path, filename, lines):
    file_path = os.path.join(path, filename) if path else filename

    content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"  # ❗ без точки

    content += "\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)

    print(f"File created/updated: {file_path}")


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d dir1 dir2 -f filename.txt")
        return

    dirs, filename = parse_args(args)
    path = create_dirs(dirs)

    if not filename:
        print(f"Directories created: {path}")
        return

    lines = get_user_input()
    write_file(path, filename, lines)


if __name__ == "__main__":
    main()
