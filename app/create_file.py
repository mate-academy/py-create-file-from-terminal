import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dirs: list[str] = []
    filename: str | None = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and args[d_index] != "-f":
            dirs.append(args[d_index])
            d_index += 1

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            filename = args[f_index]

    return dirs, filename


def main() -> None:
    args = sys.argv[1:]
    dirs, filename = parse_args(args)

    if not dirs and not filename:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    base_dir = os.getcwd()

    if dirs:
        dir_path = os.path.join(base_dir, *dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = base_dir

    if filename is None:
        return

    file_path = os.path.join(dir_path, filename)
    content_lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    if not content_lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines_to_write: list[str] = [timestamp]
    for index, text in enumerate(content_lines, start=1):
        lines_to_write.append(f"{index} {text}")

    block = "\n".join(lines_to_write) + "\n"

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(block)


if __name__ == "__main__":
    main()
