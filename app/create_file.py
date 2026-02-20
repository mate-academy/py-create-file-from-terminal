import sys
import os
from datetime import datetime


def main():
    args = sys.argv[1:]

    directory = []
    filename = None

    # parse flags
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directory.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: -f flag requires a filename.")
                return
        else:
            print(f"Unknown argument: {args[i]}")
            return

    # build the directory path if any
    dir_path = os.path.join(*directory) if directory else "."
    if directory:
        os.makedirs(dir_path, exist_ok=True)

    # handle only directory creation if no file
    if filename is None:
        print(f"Directory created: {dir_path}")
        return

    # get full path to file
    file_path = os.path.join(dir_path, filename)

    # read content lines from user
    lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # prepare content block
    block = [timestamp] + lines
    block_text = "\n".join(block) + "\n"

    # write or append to file
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(block_text + "\n")

    print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
