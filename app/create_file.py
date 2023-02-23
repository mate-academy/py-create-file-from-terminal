import sys
import os
from datetime import datetime


def read_content() -> list:
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            content.append("\n")
            break
        content.append(line)
    return content


def create_file(file_path):
    content = read_content()

    file_existed = os.path.exists(file_path)
    with open(file_path, "a+") as f:
        if not file_existed:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        f.write("\n".join(content))


def main(args):
    if "-d" in args and "-f" in args:
        dir_path = os.path.join(*args[args.index("-d")+1:args.index("-f")])
        file_name = args[args.index("-f")+1]
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)
    elif "-d" in args:
        dir_path = os.path.join(*args[args.index("-d")+1:])
        os.makedirs(dir_path, exist_ok=True)
    elif "-f" in args:
        file_path = args[args.index("-f")+1]
        create_file(file_path)


if __name__ == "__main__":
    main(sys.argv[1:])
