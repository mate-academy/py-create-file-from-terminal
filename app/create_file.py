import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument(
    "-d",
    dest="directories",
    type=str,
    nargs="*",
    help="directories name(s)"
)
parser.add_argument(
    "-f",
    dest="file",
    type=str,
    help="file name"
)

args = parser.parse_args()


dir_path = None


if args.directories:
    parent_dir = os.getcwd()
    directories = args.directories
    path = os.path.join(parent_dir, *directories)
    os.makedirs(path, exist_ok=True)
    dir_path = path

if args.file:
    input("Press enter to process file")
    file_path = os.path.join(dir_path, args.file) if dir_path else args.file
    with open(file_path, "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(str(now) + "\n")
        row_counter = 1
        while True:
            text = input("Enter content line:")
            if text == "stop":
                f.write("\n")
                break
            f.write(f"{row_counter} {text}" + "\n")
            row_counter += 1
