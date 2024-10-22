import os
import sys
from datetime import datetime


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def create_file(file_path):
    content_lines = []
    print(f"Enter content for {file_path} (enter stop for break):")

    while True:
        line = input("Enter content line: ")
        if line.lower() == 'stop':
            break
        content_lines.append(line)

    return content_lines


def write_to_file(file_path, content_lines):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as f:
        if os.path.getsize(file_path) > 0:
            f.write('\n')
        f.write(f"{timestamp}\n")
        for idx, line in enumerate(content_lines, start=1):
            f.write(f"{idx} {line}\n")


def main():
    args = sys.argv[1:]

    directory = []
    file_name = None

    for i, arg in enumerate(args):
        if arg == '-d':
            directory.extend(args[i+1:])
            break
        elif arg == '-f' and i + 1 < len(args):
            file_name = args[i + 1]

    if directory:
        path = os.path.join(*directory)
        create_directory(path)

    if file_name:
        if directory:
            file_path = os.path.join(path, file_name)
        else:
            file_path = os.path.join(os.getcwd(), file_name)

        content_lines = create_file(file_path)
        write_to_file(file_path, content_lines)


if __name__ == '__main__':
    main()
