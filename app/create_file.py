import sys
import os
from datetime import datetime


def main():
    args = sys.argv[1:]
    if not args:
        print("No arguments provided. Use -d for directories or -f for files.")
        return

    if "-d" in args:
        process_directories(args)

    if "-f" in args:
        process_file(args)


def process_directories(args):
    """
    Create directories based on -d flag
    """
    dir_index = args.index("-d") + 1
    dirs = []
    while dir_index < len(args) and args[dir_index] != "-f":
        dirs.append(args[dir_index])
        dir_index += 1

    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
    else:
        print("No directories specified after -d.")


def process_file(args):
    """
    Create or overwrite files based on -f flag
    """
    file_index = args.index("-f") + 1
    if file_index >= len(args):
        print("No file specified after -f.")
        return

    filename = args[file_index]
    content_lines = []
    print("Enter content line (type 'stop' to finish):")

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [f"{timestamp}\n"] + [f"{i + 1} {line}" for i, line in
                                            enumerate(content_lines)]

    file_path = os.path.join(".", filename)
    with open(file_path, "a") as file:
        file.writelines(formatted_lines)

    print(f"File '{file_path}' created/updated.")


if __name__ == "__main__":
    main()
