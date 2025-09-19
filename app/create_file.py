import os
import sys
import datetime


def read_the_lines() -> list[str]:
    lines = []
    line_number = 0
    while True:
        inp = input("Enter content line: ")
        if inp.lower() == "stop":
            break
        line_number += 1
        lines.append(f"{line_number} {inp}")
    return lines


def write_to_the_file(filename: str, lines: list[str], path: str = "") -> None:
    full_path = os.path.join(path, filename)
    with open(full_path, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        for line in lines:
            f.write(line + "\n")


args = sys.argv
current_dir = os.getcwd()

file_name = ""
directories: list[str] = []
path = current_dir

if "-f" in args:
    file_index = args.index("-f")
    if file_index + 1 >= len(args):
        sys.exit("Error: -f flag requires a filename.\nUsage: python create_file.py -f <filename> [-d <dirs>]")
    file_name = args[file_index + 1]


if "-d" in args:
    directory_index = args.index("-d")
    stop_index = file_index if "-f" in args else None
    directories = args[directory_index + 1:stop_index]
    path = os.path.join(current_dir, *directories)
    os.makedirs(path, exist_ok=True)

if file_name:
    lines = read_the_lines()
    write_to_the_file(file_name, lines, path)
