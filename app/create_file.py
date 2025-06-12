import sys
import os
from datetime import datetime
from typing import List


def get_input_lines() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return f"{timestamp}\n" + "\n".join(numbered_lines) + "\n"


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("No arguments provided.")
        return

    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        next_flag_index = len(args)
        if "-f" in args[d_index + 1:]:
            next_flag_index = args.index("-f")
        dir_parts = args[d_index + 1:next_flag_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    path = os.getcwd()
    if dir_parts:
        path = os.path.join(path, *dir_parts)
        os.makedirs(path, exist_ok=True)

    if file_name:
        file_path = os.path.join(path, file_name)
        lines = get_input_lines()
        content = format_content(lines)
        with open(file_path, "a", encoding="utf-8") as f:
            if os.path.getsize(file_path) > 0:
                f.write("\n" + content)
            else:
                f.write(content)


if __name__ == "__main__":
    main()
