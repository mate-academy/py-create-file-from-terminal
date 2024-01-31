import os
import sys
from datetime import datetime


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_lines() -> list:
    lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file(file_path: str,
                lines: list) -> None:
    with open(file_path, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp}\n')
        for i, line in enumerate(lines, start=1):
            f.write(f'{i} {line}\n')


def main() -> None:
    dir_flag = '-d' in sys.argv
    file_flag = '-f' in sys.argv

    if dir_flag and file_flag:
        dir_index = sys.argv.index('-d')
        file_index = sys.argv.index('-f')
        dir_path = os.path.join(*sys.argv[dir_index+1:file_index])
        file_name = sys.argv[file_index+1]
    elif dir_flag:
        dir_index = sys.argv.index('-d')
        dir_path = os.path.join(*sys.argv[dir_index+1:])
        file_name = None
    elif file_flag:
        file_index = sys.argv.index('-f')
        dir_path = ''
        file_name = sys.argv[file_index+1]
    else:
        print('No valid flags passed.')
        return

    if dir_path:
        create_directory(dir_path)

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        lines = read_lines()
        create_file(file_path, lines)

if __name__ == '__main__':
    main()

