import argparse
import os
from datetime import datetime


parser = argparse.ArgumentParser(
    prog="create_file",
    description="create file from console"
)

parser.add_argument("-d", "--dir", nargs="+")
parser.add_argument("-f", "--file")

args = parser.parse_args()


def make_dirs(dirs: list) -> None:
    os.makedirs(os.path.join(*dirs), exist_ok=True)


def create_file(file_name: str) -> None:
    is_exist = os.path.isfile(file_name)

    with open(file_name, "a" if is_exist else "w") as source_file:
        line_count = 1

        if is_exist:
            source_file.write("\n")

        source_file.write(
            datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            source_file.write(f"{line_count} {new_line}\n")
            line_count += 1


if __name__ == "__main__":
    if args.dir is not None:
        make_dirs(args.dir)
        if args.file is not None:
            create_file(file_name=os.path.join(*args.dir, args.file))
    elif args.file is not None:
        create_file(file_name=args.file)
