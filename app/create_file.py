import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_args() -> Tuple[List[str], Optional[str]]:
    args = sys.argv[1:]
    dir_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        next_flag = args[d_index + 1:]
        if "-f" in next_flag:
            f_index = next_flag.index("-f")
            dir_path = next_flag[:f_index]
        else:
            dir_path = next_flag

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    return dir_path, file_name


def get_content() -> str:
    lines = []
    line_num = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{line_num} {line}")
        line_num += 1
    return lines


def main() -> None:
    dir_path_parts, file_name = parse_args()

    base_path = os.getcwd()
    if dir_path_parts:
        full_dir_path = os.path.join(base_path, *dir_path_parts)
        os.makedirs(full_dir_path, exist_ok=True)
    else:
        full_dir_path = base_path

    if file_name:
        full_file_path = os.path.join(full_dir_path, file_name)
        lines = get_content()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(full_file_path, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}\n")
            for line in lines:
                f.write(f"{line}\n")
            f.write("\n")
    elif dir_path_parts:
        print(
            f"Directory created at: "
            f"{os.path.join(base_path, *dir_path_parts)}"
        )
    else:
        print("Error: No valid flags provided. Use -d and/or -f.")


if __name__ == "__main__":
    main()
