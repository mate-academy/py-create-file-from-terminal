import os
import sys
import datetime
from typing import Any, LiteralString


def parse_args() -> tuple[list[Any], str]:
    args = sys.argv[1:]
    list_dirs = []
    i = 0
    filename = None
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                list_dirs.append(args[i])
                i += 1

        elif args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
            else:
                raise (Exception("No filename given"))
        else:
            i = i + 1
    return list_dirs, filename


def create_directory(list_dirs: list[str]) -> LiteralString | str | bytes:
    if list_dirs:
        path = os.path.join(*list_dirs)
        os.makedirs(path, exist_ok=True)
    else:
        path = "."
    return path


def collect_lines() -> list[Any]:
    lines = []
    count = 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{count} {line}")
        count += 1
    return lines


def prepare_content(lines: list[Any]) -> tuple[str, LiteralString]:
    current_date = datetime.datetime.now()
    header = current_date.strftime("%Y-%m-%d %H:%M:%S")
    body = "\n".join(lines)
    return header, body


def write_to_file(full_path: Any, header: str, body: LiteralString) -> None:
    prefix = ""
    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        prefix = "\n\n"

    final = prefix + header + "\n" + body + "\n"

    with open(full_path, "a", encoding="utf-8") as target_file:
        target_file.write(final)


def main_func() -> None:
    list_dirs, filename = parse_args()
    path = create_directory(list_dirs)
    if not filename:
        print("Created only directories: ", path)
        sys.exit(0)

    full_path = os.path.join(path, filename)
    lines = collect_lines()
    header, body = prepare_content(lines)
    write_to_file(full_path, header, body)


if __name__ == "__main__":
    main_func()
