import os
import os.path
import sys
from datetime import datetime


def split_command():
    command = sys.argv[1:]
    file_name = None
    directories = None

    if "-f" in command:
        file_name = command[-1]
        command = command[:-2]
    if "-d" in command:
        directories = command[1:]
    return file_name, directories


def create_directory(directories):
    path = "/".join(directories)

    try:
        os.makedirs("/".join(directories))
    except FileExistsError:
        print("directory is already exists")

    return path


def create_file(path, file_name):
    content = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)

    file_path = f"{path}/{file_name}" if path else file_name
    is_exists = False
    if os.path.exists(file_path):
        is_exists = True

    with open(file_path, "a") as f:
        if is_exists:
            f.write("\n")
        f.write(f"{datetime.now().strftime('%Y-%m-%d %X')}\n")
        for i in range(len(content)):
            f.write(f"{i + 1} {content[i]}\n")


def execute_command():
    file_name, directories = split_command()
    path = ""
    if directories:
        path = create_directory(directories)
    if file_name:
        create_file(path, file_name)


if __name__ == '__main__':
    execute_command()
