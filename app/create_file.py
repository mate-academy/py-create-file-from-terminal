import sys
import os
import datetime


args = sys.argv[1:]


def create_file() -> None:
    try:
        d_index = args.index("-d")
    except ValueError:
        d_index = None
    try:
        f_index = args.index("-f")
    except ValueError:
        f_index = None
    dirs = []
    filename = None
    if d_index is not None:
        start = d_index + 1
        if f_index is not None and f_index > d_index:
            end = f_index
        else:
            end = len(args)
        dirs = args[start:end]
    if f_index is not None and f_index + 1 < len(args):
        filename = args[f_index + 1]
    if dirs:
        dir_path = os.path.join(*dirs)
    else:
        dir_path = os.getcwd()
    os.makedirs(dir_path, exist_ok=True)
    if filename is None:
        return
    full_path = os.path.join(dir_path, filename)
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        elif line != "":
            lines.append(line)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for i, ln in enumerate(lines, 1):
            f.write(f"{i} {ln}\n")
        f.write("\n")
