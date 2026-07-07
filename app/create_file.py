import argparse
import os
import datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append timestamped, numbered lines to a file.")
    parser.add_argument(
        "-f", dest="filename", default=None, help="Filename to write to")
    parser.add_argument(
        "-d", dest="dirs", nargs="+",
        default=[], help="Directory path components")
    return parser.parse_args()


def create_file() -> None:
    args = parse_args()

    if args.dirs:
        dir_path = os.path.join(*args.dirs)
        os.makedirs(dir_path, exist_ok=True)

    if args.filename is None:
        print("No filename provided")
        return

    filepath = os.path.join(*args.dirs, args.filename) \
        if args.dirs else args.filename

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{len(lines) + 1} {line}")

    file_exists = os.path.exists(filepath)

    with open(filepath, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in lines:
            f.write(line + "\n")


create_file()
