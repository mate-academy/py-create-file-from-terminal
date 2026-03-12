import os
import sys
from datetime import datetime
from typing import Optional


def parse_args(args: list[str]) -> tuple[Optional[str], Optional[str]]:
    dir_parts: list[str] = []
    filename: Optional[str] = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and args[d_index] != "-f":
            dir_parts.append(args[d_index])
            d_index += 1

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            filename = args[f_index]

    dir_path = os.path.join(*dir_parts) if dir_parts else None
    return dir_path, filename


def main() -> None:
    args = sys.argv[1:]
    dir_path, filename = parse_args(args)

    if dir_path is not None:
        os.makedirs(dir_path, exist_ok=True)

    if filename is None:
        return

    if dir_path is not None:
        target_path = os.path.join(dir_path, filename)
    else:
        target_path = filename

    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(target_path, "a", encoding="utf-8") as f:
        try:
            f.seek(0, 2)
            if f.tell() > 0:
                f.write("\n")
        except OSError:
            pass

        f.write(f"{timestamp}\n")
        for index, content in enumerate(lines, start=1):
            f.write(f"{index} {content}\n")


if __name__ == "__main__":
    main()
