import sys
import os
from typing import Any
from datetime import datetime


def parse_arguments(args: Any) -> Any:
    dirs = []
    file_name = None
    mode = None

    for arg in args[1:]:
        if arg == "-d":
            mode = "dir"
        elif arg == "-f":
            mode = "file"
        else:
            if mode == "dir":
                dirs.append(arg)
            elif mode == "file":
                file_name = arg

    return dirs, file_name


def get_user_content() -> Any:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(final_path: Any, lines: Any) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    need_blank_line = False
    if os.path.exists(final_path):
        if os.path.getsize(final_path) > 0:
            need_blank_line = True

    with open(final_path, "a") as f:
        if need_blank_line:
            f.write("\n")

        f.write(current_time + "\n")

        for index, content in enumerate(lines, start=1):
            f.write(f"{index} {content}\n")


def main() -> None:
    dirs, file_name = parse_arguments(sys.argv)

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name:
        if dir_path:
            final_path = os.path.join(dir_path, file_name)
        else:
            final_path = file_name

        user_lines = get_user_content()
        write_to_file(final_path, user_lines)

main()