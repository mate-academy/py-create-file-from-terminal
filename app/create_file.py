import datetime
import os
import sys


def parse_arguments(args):
    dir_path = "."
    file_name = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        if "-f" in args:
            file_index = args.index("-f")
            if dir_index < file_index:
                directories = args[dir_index:file_index]
            else:
                directories = args[dir_index:]
        else:
            directories = args[dir_index:]
        dir_path = os.path.join(*directories)

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index >= len(args):
            print("Error: No file name provided after -f")
            sys.exit(1)
        file_name = args[file_index]

    return dir_path, file_name

def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def write_to_file(file_path):
    date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{date_today}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1

if __name__ == "__main__":
    args = sys.argv[1:]
    dir_path, file_name = parse_arguments(args)

    if dir_path != ".":
        create_directory(dir_path)

    if file_name:
        file_path = os.join(dir_path, file_name)
        write_to_file(file_path)
