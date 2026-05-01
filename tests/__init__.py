import sys
import os
from datetime import datetime


def create_directory(dirs):
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")
    return path


def create_file(file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n"

    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content += f"{line_number} {line}\n"
        line_number += 1

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n\n")
        f.write(content)


def main():
    args = sys.argv[1:]

    dirs = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        try:
            filename = args[f_index + 1]
        except IndexError:
            print("Error: No filename provided after -f")
            return

    path = create_directory(dirs)

    if dirs and not filename:
        return

    if filename:
        file_path = os.path.join(path, filename) if path else filename
        create_file(file_path)


if __name__ == "__main__":
    main()