import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_content_lines() -> list[str]:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directory_parts = args[d_index + 1:f_index]
        else:
            directory_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if directory_parts:
        dir_path = os.path.join(*directory_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name is None:
        return

    file_path = os.path.join(dir_path, file_name)

    content_lines = get_content_lines()

    if not content_lines:
        return

    timestamp = get_timestamp()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
