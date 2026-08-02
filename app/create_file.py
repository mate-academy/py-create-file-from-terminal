import sys
import os
from datetime import datetime


def get_dir_name() -> list:
    args = sys.argv[1:]
    if "-f" in args and "-d" in args:
        if args.index("-f") > args.index("-d"):
            return args[args.index("-d") + 1 : args.index("-f")]
        else:
            return args[args.index("-d") + 1:]
    else:
        if "-d" in args:
            return args[args.index("-d") + 1:]
        return []


def create_dir(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def file_entry(file_path: str) -> None:
    lines = []
    if os.path.isfile(file_path):
        method = "a"
        lines.append("\n")
    else:
        method = "w"

    with open(file_path, method) as file:
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.writelines(lines)
                break
            lines.append(f"{count} {line}\n")
            count += 1


if "-d" in sys.argv and "-f" not in sys.argv:
    directories = get_dir_name()
    create_dir(directories)

if "-f" in sys.argv and "-d" not in sys.argv:
    if sys.argv.index("-f") != len(sys.argv) - 1:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        file_path = os.path.join(os.getcwd(), file_name)
        file_entry(file_path)

if "-d" in sys.argv and "-f" in sys.argv:
    directories = get_dir_name()
    file_name = sys.argv[sys.argv.index("-f") + 1]
    create_dir(directories)
    file_path = os.path.join(*directories, file_name)
    file_entry(file_path)
