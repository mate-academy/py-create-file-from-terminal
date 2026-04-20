import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    dirs_path = os.path.join(*directories) if directories else ""
    os.makedirs(dirs_path, exist_ok=True)
    return dirs_path


def return_filename(args: list) -> str:
    dirs = []
    filename = ""
    if "-d" in args and "-f" in args:
        dirs = args[args.index("-d") + 1:args.index("-f")]
        filename = args[args.index("-f") + 1]
    elif "-d" in args:
        dirs = args[args.index("-d") + 1:]
    elif "-f" in args:
        if args.index("-f") + 1 < len(args):
            return args[args.index("-f") + 1]
        raise ValueError("No file name specified")

    path_dirs = create_path(dirs)
    if filename:
        return os.path.join(path_dirs, filename)


def create_file(filename: str) -> None:
    if not filename:
        return
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    with open(filename, "a+") as file:
        file.write(datetime_now)
        idx = 1
        while True:
            print("Enter content line: ", end="")
            content = input()
            if content == "stop":
                file.write("\n")
                return
            file.write(f"{idx} {content}\n")
            idx += 1


if __name__ == "__main__":
    parse_argv = sys.argv

    filepath = return_filename(parse_argv)
    create_file(filepath)
