import argparse
import datetime
import os
from typing import List

def parse_arguments() -> argparse.Namespace:
parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="*", default=[])
parser.add_argument("-f", default=None)
return parser.parse_args()

def collect_content_lines() -> List[str]:
lines: List[str] = []
while True:
line = input("Enter content line: ")
if line == "stop":
break
lines.append(line)
return lines

def write_to_file(file_path: str, lines: List[str]) -> None:
timestamp = datetime.datetime.now().strftime(
"%Y-%m-%d %H:%M:%S"
)
file_exists = os.path.exists(file_path)
is_not_empty = file_exists and os.path.getsize(file_path) > 0

with open(file_path, "a", encoding="utf-8") as target_file:
    if is_not_empty:
        target_file.write("\n")
    target_file.write(f"{timestamp}\n")
    for index, line in enumerate(lines, start=1):
        target_file.write(f"{index} {line}\n")


def main() -> None:
args = parse_arguments()
directories = args.d
file_name = args.f

if directories:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    if directories:
        file_path = os.path.join(*(directories + [file_name]))
    else:
        file_path = file_name

    lines = collect_content_lines()
    write_to_file(file_path, lines)


if name == "main":
main()
