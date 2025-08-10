import argparse
import os
import datetime


parser = argparse.ArgumentParser(
    description="Create a file or directory with content"
)
parser.add_argument(
    "-d", "--directory", nargs="+", help="create directory with the given path"
)
parser.add_argument(
    "-f", "--file", type=str, help="create file with the given name"
)

args = parser.parse_args()

if args.directory:
    dir_path = os.path.join(*args.directory)
    os.makedirs(dir_path, exist_ok=True)

if args.file:
    file_path = args.file
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    if args.directory:
        dir_path = os.path.join(*args.directory)
        file_path = os.path.join(dir_path, file_path)

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for i, line_number in enumerate(content):
            file.write(f"{i + 1} {line_number}\n")
        file.write("\n")
