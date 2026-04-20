import sys
import os
from datetime import datetime
from typing import List


def read_content() -> List[str]:
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(filepath: str, lines: List[str]) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists_and_is_not_empty = (os.path.exists(filepath)
                                    and os.path.getsize(filepath) > 0)

    with open(filepath, "a", encoding="utf-8") as f:
        if file_exists_and_is_not_empty:
            f.write("\n")

        f.write(f"{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args: List[str] = sys.argv[1:]

    dir_path: str = ""
    filename: str = ""
    has_f_flag: bool = False

    if "-d" in args:
        d_index: int = args.index("-d")
        dirs: List[str] = []
        i: int = d_index + 1
        while i < len(args) and args[i].startswith("-") is False:
            dirs.append(args[i])
            i += 1
        dir_path: str = os.path.join(*dirs) if dirs else ""

    if "-f" in args:
        has_f_flag = True
        f_index: int = args.index("-f")

        if f_index + 1 >= len(args):
            print("Error: file name is required"
                  "immediately after the -f flag.")
            return

        filename: str = args[f_index + 1]

    if dir_path and not has_f_flag:
        os.makedirs(dir_path, exist_ok=True)
        return

    if has_f_flag:
        if not filename:
            print("Error: file name is required with -f flag.")
            return

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            filepath: str = os.path.join(dir_path, filename)
        else:
            filepath = filename

        lines: List[str] = read_content()
        write_content(filepath, lines)

    else:
        print("Error: file name is required with -f "
              "flag or use -d to create directories only.")
        return
