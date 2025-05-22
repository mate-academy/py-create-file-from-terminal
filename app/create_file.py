import sys
import os
from datetime import datetime


def create_directory(dir_parts: list[str]) -> str:
    path = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def prompt_for_content() -> list[str]:
    lines: list[str] = []
    line_num = 1
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        lines.append(f"{line_num} {user_input}")
        line_num += 1
    return lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for line in content_lines:
            f.write(line + "\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    dir_parts: list[str] = ["dir1", "dir2"]
    file_name: str = "file.txt"

    if "-d" in args:
        d_index = args.index("-d")
        next_flag_index = (
            args.index("-f")
            if "-f" in args and args.index("-f") > d_index
            else len(args)
        )
        dir_parts = args[d_index + 1:next_flag_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    base_path = os.getcwd()
    if dir_parts:
        base_path = create_directory(dir_parts)

    if file_name:
        file_path = os.path.join(base_path, file_name)
        content = prompt_for_content()
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
