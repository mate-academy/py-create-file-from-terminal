import os
import sys
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def get_content_lines() -> list[str]:
    lines = []
    count = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop" :
            break
        lines.append(f"{count} {line}")
        count += 1
    return lines


def write_to_file(path: str, lines: list[str]) -> None:
    with open(path, "a") as f:
        f.write(get_timestamp() + "\n")
        for line in lines:
            f.write(line + "\n")
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            dir_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    full_path = os.path.join(*dir_parts) if dir_parts else ""
    if full_path and not os.path.exists(full_path):
        os.makedirs(full_path)

    if file_name:
        full_path = os.path.join(full_path, file_name)
        lines = get_content_lines()
        write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
