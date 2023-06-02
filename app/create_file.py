import os
import sys
from datetime import datetime


def main():
    args = sys.argv
    if '-d' in args:
        dir_index = args.index('-d')
        directory_path = os.path.join(*args[dir_index+1:])
        if '-f' in args:
            file_index = args.index('-f')
            file_name = args[file_index+1]
            file_path = os.path.join(directory_path, file_name)
            create_file(file_path)
    elif '-f' in args:
        file_index = args.index('-f')
        file_name = args[file_index+1]
        create_file(file_name)


def create_directory(path):
    os.makedirs(path)
    print(f"Directory created: {path}")


def create_file(file_name):
    if os.path.exists(file_name):
        mode = 'a'
    else:
        mode = 'w'

    with open(file_name, mode) as file:
        file.write(datetime.now().strftime("&Y-%m-%d, %H:%M:%S\n"))
        while True:
            num = 0
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(str(num) + " " + content + "\n")
