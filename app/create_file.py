import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d",
    type=str,
    help="Create new dir",
    nargs="+", default=[],
)
parser.add_argument(
    "-f",
    type=str,
    help="Create file",
)

args = parser.parse_args()

create_file = args.f
create_folders = args.d
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if create_folders:
    os.makedirs("/".join(args.d))

if create_file:
    count_lines = 1
    with open(os.path.join("/".join(create_folders), create_file), "a") as f:
        f.write(f"{timestamp}\n")

        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            f.write(f"{count_lines} {line}\n")
            count_lines += 1
