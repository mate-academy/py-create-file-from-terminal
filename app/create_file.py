import argparse
import os
from datetime import datetime


def writing_file(full_path: str) -> None:
    with open(full_path, "a") as file:
        file.write(f"{str(datetime.today()).rsplit('.')[0]}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", help="directories name")
    parser.add_argument("-f", help="name of a file")
    args = parser.parse_args()
    args.d = "/".join(args.d)

    if args.d and not args.f:
        os.makedirs(args.d, exist_ok=True)

    if args.f and not args.d:
        writing_file(args.f)

    if args.d and args.f:
        os.makedirs(args.d, exist_ok=True)
        path_to_file = os.path.join(args.d, args.f)
        writing_file(path_to_file)
