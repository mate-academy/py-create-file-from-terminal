import sys
import os
from datetime import datetime


def create_directory(path_parts):
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def create_file(file_path):
    print(f"Creating file: {file_path}")
    with open(file_path, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)

        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")
        print(f"File '{file_path}' updated successfully.")


def main():
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        path_parts = []
        f_index = sys.argv.index("-f") if "-f" in sys.argv else None

        if f_index:
            path_parts = sys.argv[d_index + 1:f_index]
        else:
            path_parts = sys.argv[d_index + 1:]
            create_directory(path_parts)
            return

        create_directory(path_parts)
        file_name = sys.argv[f_index + 1]
        file_path = os.path.join(*path_parts, file_name)
        create_file(file_path)

    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        create_file(file_name)
    else:
        print("Usage: python create_file.py [-d dir1 dir2] -f filename")


if __name__ == "__main__":
    main()
