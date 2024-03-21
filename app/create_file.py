import os
from datetime import datetime
import sys


def write_content(file_path):
    content = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == 'stop':
            break
        content.append(line)

    with open(file_path, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content, 1):
            file.write(f"{i} {line}\n")


def create_file(file_name):
    if os.path.exists(file_name):
        write_content(file_name)
    else:
        with open(file_name, 'w') as file:
            write_content(file_name)


def create_file_with_directory(directory_path, file_name):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_path = os.path.join(directory_path, file_name)
    create_file(file_path)


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d directory_path] [-f file_name]")
        return

    if '-d' in args:
        directory_index = args.index('-d') + 1
        directory_path = os.path.join(*args[directory_index:])
        if '-f' in args:
            file_index = args.index('-f') + 1
            file_name = args[file_index]
            create_file_with_directory(directory_path, file_name)
        else:
            os.makedirs(directory_path)
    elif '-f' in args:
        file_index = args.index('-f') + 1
        file_name = args[file_index]
        create_file(file_name)
    else:
        print("Usage: python create_file.py [-d directory_path] [-f file_name]")


if __name__ == "__main__":
    main()
