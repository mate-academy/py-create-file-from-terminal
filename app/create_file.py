import argparse
import sys
import os
from datetime import datetime

def parse_arguments():
    directories = []
    filename = None

    if '-d' in sys.argv:
        d_index = sys.argv.index('-d')
        for arg in sys.argv[d_index + 1:]:
            if arg.startswith("-"):
                break
            directories.append(arg)

    if '-f' in sys.argv:
        f_index = sys.argv.index('-f')
        filename = sys.argv[f_index + 1]

    return directories, filename


def create_directories(directories):
    if not directories:
        return ""
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_file_content():
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path, content_lines):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exist_and_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as f:
        if file_exist_and_not_empty:
            f.write("\n")
        f.write(timestamp + "\n")
        for index, line in enumerate(content_lines, 1):
            f.write(f"{index} {line}\n")


def main():
    directories, filename = parse_arguments()
    dir_path = create_directories(directories)

    if filename:
        if dir_path:
            file_path = os.path.join(dir_path, filename)
        else:
            file_path = filename

        lines = get_file_content()
        write_to_file(file_path, lines)

if __name__ == "__main__":
    main()
