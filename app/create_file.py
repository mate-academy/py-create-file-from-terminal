import sys
import os
from datetime import datetime


def get_content_lines() -> list:
    lines = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp] + lines + [""]

    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n".join(content))


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        # directory arguments start after -d
        next_flag = (args[d_index + 1:].index("-f")
                     + d_index + 1) if "-f" in args[d_index + 1:]\
            else len(args)
        dir_parts = args[d_index + 1:next_flag]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: No file name provided after -f flag")
            return

    if file_name:
        file_path = os.path.join(dir_path, file_name) \
            if dir_path else file_name
        lines = get_content_lines()
        write_to_file(file_path, lines)
        print(f"File written to: {file_path}")
    elif dir_path:
        print(f"Directory created: {dir_path}")
    else:
        print("Error: No valid flags provided.")


if __name__ == "__main__":
    main()
