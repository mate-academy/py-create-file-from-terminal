import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+")
parser.add_argument("-f")
args = parser.parse_args()

path_dir = None
if args.d:
    path_dir = os.path.join(*args.d)
    os.makedirs(path_dir, exist_ok=True)

if args.f:
    path_file = os.path.join(path_dir, args.f) if path_dir else args.f

    file_has_content = (
        os.path.exists(path_file) and os.path.getsize(path_file) > 0
    )

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
