import os
import sys
import datetime


def create_path() -> str:
    args = sys.argv

    index_of_dir = args.index("-d") + 1
    path_parts = []

    while index_of_dir < len(args) and not args[index_of_dir].startswith("-"):
        path_parts.append(args[index_of_dir])
        index_of_dir += 1
    path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> str:
    filename = args[args.index("-f") + 1]
    full_path = os.path.join(file_path, filename)
    with open(full_path, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 0
        string = input("Enter content line: ")
        while string != "stop":
            count += 1
            f.write(f"{count} " + string + "\n")
            string = input("Enter content line: ")
        f.write("\n")
    return filename


args = sys.argv

if "-d" in args and "-f" in args:
    path = create_path()
    create_file(path)
elif "-d" in args:
    create_path()
elif "-f" in args:
    create_file(os.getcwd())
