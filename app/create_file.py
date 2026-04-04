import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    path_dir = None
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        dir_parts = []
        for item in args[d_index:]:
            if item.startswith("-"):
                break
            dir_parts.append(item)
        if dir_parts:
            path_dir = os.path.join(*dir_parts)

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    return path_dir, file_name


def collect_content() -> str:
    text = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text.append(timestamp)

    count = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        text.append(f"{count} {line}")
        count += 1

    return "\n".join(text) + "\n"


def write_to_file(full_path: str, content: str) -> None:
    mode = "a"
    prefix = ""

    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        prefix = "\n"

    with open(full_path, mode) as file:
        file.write(prefix + content)


def main() -> None:
    path_dir, file_name = parse_arguments(sys.argv)

    if path_dir:
        os.makedirs(path_dir, exist_ok=True)

    if file_name:
        full_path = os.path.join(path_dir, file_name) \
            if path_dir else file_name
        content = collect_content()
        write_to_file(full_path, content)


if __name__ == "__main__":
    main()
