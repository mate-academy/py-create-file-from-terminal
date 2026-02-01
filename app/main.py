import os
import sys
from datetime import datetime


def get_content() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(full_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def main() -> None:
    args = sys.argv
    directory_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for arg in args[d_index + 1:]:
            if arg == "-f":
                break
            dir_parts.append(arg)

        directory_path = os.path.join(*dir_parts)
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if file_name:
        full_path = os.path.join(directory_path, file_name)
        lines = get_content()
        write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
