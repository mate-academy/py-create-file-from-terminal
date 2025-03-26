import sys
import os
from datetime import datetime


def parse_args():
    args = sys.argv[1:]
    dir_path = []
    file_name = None

    if '-d' in args:
        d_index = args.index('-d')
        if '-f' in args:
            f_index = args.index('-f')
            dir_path = args[d_index + 1:f_index]
            file_name = args[f_index + 1] if f_index + 1 < len(args) else None
        else:
            dir_path = args[d_index + 1:]
    elif '-f' in args:
        f_index = args.index('-f')
        file_name = args[f_index + 1] if f_index + 1 < len(args) else None

    return dir_path, file_name


def create_directory(path):
    if path:
        os.makedirs(os.path.join(*path), exist_ok=True)


def write_to_file(file_path):
    print("Enter content line (type 'stop' to finish):")
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")

    print(f"Content written to {file_path}")


def main():
    dir_path, file_name = parse_args()

    if not dir_path and not file_name:
        print("Usage: python create_file.py [-d dir1 dir2] [-f filename]")
        return

    if dir_path:
        create_directory(dir_path)

    if file_name:
        full_path = os.path.join(*dir_path, file_name) \
            if dir_path else file_name
        write_to_file(full_path)


if __name__ == "__main__":
    main()

# write your code here
