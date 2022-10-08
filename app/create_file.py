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

file = args.f
folders = args.d

if folders:
    os.makedirs(os.path.join(*folders))

if file:
    count_lines = 1
    with open(os.path.join(*folders, file), "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while (line := input("Enter content line:")) != "stop":
            f.write(f"{count_lines} {line}\n")
            count_lines += 1
