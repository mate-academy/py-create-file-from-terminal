import os
import sys
import datetime


def write_to_file(path: str) -> None:
    count = 0
    if os.path.exists(path):
        with open(path, "a") as f:
            f.write("\n")
    with open(path, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        ask = input("Enter content line: ")
        while ask != "stop":
            count += 1
            f.write(f"{count} {ask}\n")
            ask = input("Enter content line: ")


parent_dir = os.getcwd()
args = sys.argv[1:]

if "-d" in args and "-f" not in args:
    idx_d = args.index("-d")
    path = os.path.join(parent_dir, *args[idx_d + 1:])
    os.makedirs(path)

elif "-f" in args and "-d" not in args:
    idx_f = args.index("-f")
    path = os.path.join(parent_dir, args[idx_f + 1])
    write_to_file(path)

elif "-d" in args and "-f" in args:
    idx_d = args.index("-d")
    idx_f = args.index("-f")
    directories = args[idx_d + 1 : idx_f] \
        if idx_d < idx_f else args[idx_d + 1:]
    filename = args[idx_f + 1] if idx_f + 1 < len(args) else args[idx_f - 1]
    os.makedirs(os.path.join(parent_dir, *directories), exist_ok=True)
    path = os.path.join(parent_dir, *directories, filename)
    write_to_file(path)
