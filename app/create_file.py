# write your code here
import os
import sys

from datetime import datetime


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list[str]) -> str:
    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_with_number = [f"{i} {line}" for i, line in enumerate(lines, start=1)]
    return "\n".join([cur_time, *line_with_number])


def create_file(file_name: str, content: str = "") -> None:
    if os.path.exists(file_name):
        with open(file_name, "a") as f:
            f.write("\n\n" + content)
    else:
        with open(file_name, "w") as f:
            f.write(content)


def create_dir(args: list[str]) -> str:
    d_flag = args.index("-d")
    if "-f" in args and args.index("-f") > d_flag:
        last = args.index("-f")
    else:
        last = len(args)
    dir_names = args[d_flag + 1:last]
    dir_path = os.path.join(*dir_names)
    os.makedirs(dir_path, exist_ok=True)

    return dir_path


def handle_create_from_terminal() -> None:
    args = sys.argv[1:]
    dir_path = ""

    if "-d" in args:
        dir_path = create_dir(args)

    if "-f" in args:
        f_flag = args.index("-f")
        file_name = args[f_flag + 1]
        lines = read_content()
        content = format_content(lines)
        res_file = os.path.join(dir_path, file_name) if dir_path else file_name
        create_file(res_file, content)


handle_create_from_terminal()
