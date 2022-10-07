import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", type=str, nargs="+", default=[])
parser.add_argument("-f", type=str, default="")

args = parser.parse_args()

dire = args.d
file_name = args.f
complete_name = os.path.join("/".join(dire), file_name)
date = datetime.now().strftime("%Y-%m-%d %I:%M:%S")

if dire:
    os.makedirs("/".join(dire))

if file_name:
    with open(complete_name, "a") as f:
        f.write(f"{date}\n")

        while (line := input("Enter content line: ")) != "stop":
            f.write(f"{line}\n")
