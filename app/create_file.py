import datetime
import os
import sys


def parse_arguments() -> tuple[list[str], str | None]:
    d_name: list[str] = []
    f_name: str | None = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                d_name.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                f_name = args[i]
                i += 1
        else:
            i += 1

    return d_name, f_name


def read_lines_from_input() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip() == "stop":
            break
        lines.append(line.strip())
    return lines


def create_file_and_content(file_path: str) -> None:
    dir_path = os.path.dirname(file_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_exists = os.path.exists(file_path)
    lines = read_lines_from_input()

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    d_name, f_name = parse_arguments()

    if f_name:
        path = os.path.join(*d_name, f_name) if d_name else f_name
        create_file_and_content(path)
    elif d_name:
        os.makedirs(os.path.join(*d_name), exist_ok=True)


main()
