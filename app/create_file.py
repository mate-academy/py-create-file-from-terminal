import sys
import os
from datetime import datetime

argv = sys.argv[1:]

args_d = []
arg_f = None

if "-d" in argv:
    idx = argv.index("-d") + 1
    while idx < len(argv) and not argv[idx].startswith("-"):
        args_d.append(argv[idx])
        idx += 1

if "-f" in argv:
    idx = argv.index("-f") + 1
    if idx < len(argv):
        arg_f = argv[idx]

path_dir = None
if args_d:
    path_dir = os.path.join(*args_d)
    os.makedirs(path_dir, exist_ok=True)

if arg_f:
    path_file = os.path.join(path_dir, arg_f) if path_dir else arg_f

    file_exists = os.path.exists(path_file)
    file_has_content = file_exists and os.path.getsize(path_file) > 0

    with open(path_file, "a") as f:
        if file_has_content:
            f.write("\n")
        current = datetime.now()
        f.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")

    order = 0
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        order += 1
        with open(path_file, "a") as f:
            f.write(f"{order} {line}\n")
