import datetime
import os
from argparse import ArgumentParser


parser = ArgumentParser(description="Create file with timestamped content.")

parser.add_argument("-d", nargs="+", help="Path components for directory")
parser.add_argument("-f", help="Filename to create or append to")

args = parser.parse_args()

if not args.f:
    parser.error("Missing filename. Use -f <filename> to specify file.")


if not args.d:
    parser.error("Missing directory path. Use -d dir1 dir2 to specify folder.")
else:
    os.makedirs(os.path.join(*args.d))
    file_path = os.path.join(*args.d, args.f) if args.d else args.f
    with open(file_path, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1
