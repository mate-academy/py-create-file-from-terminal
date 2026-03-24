import sys
import os
from datetime import datetime
from typing import List


def main() -> None:
    args: List[str] = sys.argv[1:]

    has_d = "-d" in args
    has_f = "-f" in args
    if not has_f:
        return
    f_index = args.index("-f")
    file_name: str = args[f_index + 1]
    dirs: List[str] = []
    if has_d:
        d_index = args.index("-d")
        for item in args[d_index + 1:]:
            if item == "-f":
                break
            dirs.append(item)
    path: str = ""
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [
        f"{i + 1} {line}" for i, line in enumerate(lines)
    ]
    full_path: str = (
        os.path.join(path, file_name) if path else file_name
    )
    file_exists = os.path.exists(full_path)

    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(timestamp + "\n")

        for line in formatted_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
