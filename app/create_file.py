import argparse
import os
from datetime import datetime

current_directory = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directories", help="makes directories", nargs="+")
parser.add_argument("-f", "--file", help="creates file")
args = parser.parse_args()

if args.directories:
    current_directory = os.path.join(current_directory, *args.directories)
    os.makedirs(current_directory, exist_ok=True)

if args.file:
    with (open(os.path.join(current_directory, args.file), "a")
          as file_with_lines):
        file_with_lines.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        line_number = 1
        while True:
            line_for_file = input("Enter content line:")
            if line_for_file == "stop":
                break
            file_with_lines.write(f"{line_number} {line_for_file}\n")
            line_number += 1
