import os
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+")
parser.add_argument("-f")
args = parser.parse_args()

if args.d:
    os.makedirs(os.path.join(*args.d), exist_ok=True)

if args.f:
    file_path = os.path.join(*args.d, args.f) if args.d else args.f
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        line_count = 0
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                file.write("\n")
                break
            line_count += 1
            file.write(f"{line_count} {new_line}\n")
