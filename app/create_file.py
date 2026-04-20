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

file_name = args.f
folders = args.d

if folders:
    os.makedirs(os.path.join(*folders))

if file_name:
    count_lines = 1
    empty_line = "\n"
    with open(os.path.join(*folders, file_name), "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            line = input("Enter content line:")
            if line == "stop":
                f.write(empty_line)
                break
            f.write(f"{count_lines} {line}\n")
            count_lines += 1
