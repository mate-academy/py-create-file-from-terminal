import sys
import os
from datetime import datetime
from typing import List


def parse_args() -> tuple[str, str]:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        next_flag = args[d_index + 1:]
        if "-f" in next_flag:
            f_index = next_flag.index("-f")
        else:
            f_index = len(next_flag)
        path_parts = next_flag[:f_index]
        dir_path = os.path.join(*path_parts)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: Missing filename after -f flag")
            sys.exit(1)

    return dir_path, file_name


def collect_content() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(path: str, content: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    dir_path, file_name = parse_args()

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if not file_name:
        print("No file specified. Exiting.")
        return

    full_path = os.path.join(dir_path, file_name) if dir_path else file_name
    content = collect_content()
    write_to_file(full_path, content)
    print(f"Content written to {full_path}")


if __name__ == "__main__":
    main()
