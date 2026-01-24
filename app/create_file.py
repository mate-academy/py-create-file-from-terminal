import os
import argparse
from datetime import datetime


def create_file(file_name: str | bytes) -> None:
    input_data = input("Enter content line: ")

    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        number_line = 1
        while input_data != "stop":
            f.write(f"{number_line} {input_data} \n")
            number_line += 1
            input_data = input("Enter content line: ")

        f.write("\n")


def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", nargs=1)
    parser.add_argument("-d", nargs="+")
    return parser.parse_args()


def main() -> None:
    args = argument_parser()

    if args.f and args.d:
        dirs_path = os.path.join(*args.d)
        file_path = os.path.join(*args.d, args.f[0])

        if not os.path.exists(dirs_path):
            os.makedirs(dirs_path)

        create_file(file_path)
    elif args.f:
        file_path = os.path.join(args.f[0])
        create_file(file_path)
    elif args.d:
        dirs_path = os.path.join(*args.d)
        if not os.path.exists(dirs_path):
            os.makedirs(dirs_path)
    else:
        print("Enter: -f for file name or/and -d for directories name")


main()
