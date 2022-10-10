import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", type=str, nargs="+", default=[])
parser.add_argument("-f", type=str, default="")

args = parser.parse_args()

directory_name = args.d
file_name = args.f
complete_name = os.path.join("/".join(directory_name), file_name)
date = datetime.now().strftime("%Y-%m-%d %I:%M:%S")

if directory_name:
    os.makedirs("/".join(directory_name))

if file_name:
    with open(os.path.join(complete_name), "a") as f:

        number_of_line = 1
        text = ""

        while (line := input("Enter content line: ")) != "stop":
            text += f"{number_of_line} {line}\n"
            number_of_line += 1

        if text:
            f.write(f"{date}\n{text}\n")
