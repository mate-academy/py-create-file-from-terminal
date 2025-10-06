import os
import sys
from datetime import datetime


def create_file_with_content(full_path: str) -> None:
    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)
        except EOFError:
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_block = [timestamp]
    for i, line in enumerate(lines, 1):
        content_block.append(f"{i} {line}")

    with open(full_path, "a", encoding="utf-8") as f:
        if f.tell() > 0:
            f.write("\n\n")

        f.write("\n".join(content_block))


def main() -> None:
    args = sys.argv[1:]

    if not args:
        return

    dir_parts = []
    file_name = None

    try:
        if "-d" in args:
            d_index = args.index("-d")
            end_index = ""
            if "-f" in args[d_index:]:
                end_index = args.index("-f")
            else:
                end_index = len(args)
            dir_parts = args[d_index + 1:end_index]

        if "-f" in args:
            f_index = args.index("-f")
            if f_index + 1 < len(args):
                file_name = args[f_index + 1]
            else:
                return

    except (ValueError, IndexError):
        return

    directory_path = os.path.join(*dir_parts) if dir_parts else "."

    if directory_path != ".":
        try:
            os.makedirs(directory_path, exist_ok=True)
        except OSError:
            return

    if file_name:
        full_path = os.path.join(directory_path, file_name)
        create_file_with_content(full_path)


if __name__ == "__main__":
    main()
