import os
import sys

from datetime import datetime

args = sys.argv[1:]


def get_flag_index(args: list[str], flag: str) -> int | None:
    if flag in args:
        return args.index(flag)
    return None


d_flag_index = get_flag_index(args, "-d")
f_flag_index = get_flag_index(args, "-f")


def get_args_after_flag(
    args: list[str],
    flag_index: int | None,
    next_flag_index: int | None
) -> list[str]:
    if flag_index is None:
        return []

    start_index = flag_index + 1
    end_index = next_flag_index if next_flag_index is not None else len(args)
    return args[start_index:end_index]


directories = get_args_after_flag(args, d_flag_index, f_flag_index)
filename = get_args_after_flag(args, f_flag_index, None)
filename = filename[0] if filename else None

if d_flag_index is not None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

if f_flag_index is not None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_path = (os.path.join(*directories, filename) if directories
                 else filename)

    with open(file_path, "w") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")
