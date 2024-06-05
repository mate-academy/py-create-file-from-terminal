import os
import datetime
from sys import argv


def create_file(path, filename, content):
    full_path = os.path.join(path, filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(full_path, "a") as f:
            if not os.path.exists(full_path):
                f.write(f"{timestamp}\n")
            for i, line in enumerate(content, 1):
                f.write(f"{i} {line}\n")
        print(f"File created successfully: {full_path}")
    except FileNotFoundError:
        print(f"Error: Directory {path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to create file or directory.")


def get_content():
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def main():
    if len(argv) < 3:
        print("Python create_file.py [-d dir1 dir2] -f filename")
        return
    create_dir = False
    dir_path = ""
    for i, arg in enumerate(argv[1:]):
        if arg == "-d":
            create_dir = True
            dir_path = os.path.join(dir_path, argv[i + 2])
        elif arg == "-f":
            filename = argv[i + 2]
        else:
            print(f"Invalid argument: {arg}")
            return
    if create_dir:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created successfully: {dir_path}")
        except PermissionError:
            print(f"Error: Permission denied to create directory.")
            return
    content = get_content()
    create_file(dir_path, filename, content)


if __name__ == "__main__":
    main()
