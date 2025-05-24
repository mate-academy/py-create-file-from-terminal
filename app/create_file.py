import sys
import os
from datetime import datetime


def get_content_lines() -> list[str]:
    lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1
    return lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")


def main() -> None:
    args = sys.argv[1:]

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        next_flag = len(args)
        if "-f" in args:
            next_flag = args.index("-f")
        dir_parts = args[d_index + 1:next_flag]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            print("Error: Missing file name after -f flag.")
            return
        file_name = args[f_index + 1]

        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        content = get_content_lines()
        write_to_file(file_path, content)
        print(f"File saved at: {file_path}")

    elif "-d" in args and not file_name:
        print(f"Directory created at: {os.path.abspath(dir_path)}")


if __name__ == "__main__":
    main()
