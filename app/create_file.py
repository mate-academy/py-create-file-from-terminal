import sys
import os
from datetime import datetime

current_dir = os.getcwd()
os.chdir(current_dir)
print("Content: ", sys.argv)


def parse_directory_files():
    args = sys.argv[1:]
    i = 0
    directory = ""
    file = ""
    while i < len(args):
        if args[i] == "-d":
            i += 1
            dir_parts = []
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            if dir_parts:
                directory = os.path.join(*dir_parts)
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                file = args[i]
            i += 1
        else:
            i += 1
    return directory, file


def create_file(file):
    with open(file, "a") as f:
        while True:
            new_str = input("Enter content line: ")
            if new_str == "stop":
                break
            new_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line_number = sum(1 for _ in open(file)) + 1
            f.write(f"{new_time}\n{line_number} {new_str}\n")


def main():
    directory, file = parse_directory_files()

    if directory:
        os.makedirs(directory, exist_ok=True)

    if file:
        file_path = os.path.join(directory, file) if directory else file
        create_file(file_path)


if __name__ == "__main__":
    main()
