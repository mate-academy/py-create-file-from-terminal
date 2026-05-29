import sys
import os
from typing import Any
from datetime import datetime


def parse_arguments(args: Any) -> Any:
    dirs = []
    file_name = None

    has_d = "-d" in args
    has_f = "-f" in args

    if has_d:
        d_idx = args.index("-d")
        if has_f and args.index("-f") > d_idx:
            dirs = args[d_idx + 1: args.index("-f")]
        else:
            dirs = args[d_idx + 1:]

    if has_f:
        f_idx = args.index("-f")
        if has_d and args.index("-d") > f_idx:
            f_slice = args[f_idx + 1: args.index("-d")]
        else:
            f_slice = args[f_idx + 1:]

        if f_slice:
            file_name = f_slice[0]

    return dirs, file_name


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

        user_lines = []
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            user_lines.append(f"{line_num} {line}\n")
            line_num += 1

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(final_path, "a") as f:
            if os.path.exists(final_path) and os.path.getsize(final_path) > 0:
                f.write("\n")

            f.write(f"{current_time}\n")
            f.writelines(user_lines)

main()
