import argparse
import os
import sys
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", type=str)
    parser.add_argument("-f", type=str)
    args = parser.parse_args(sys.argv[1:])

    if not args.d and not args.f:
        raise ValueError("At leas one flag should be specified: -d or -f")

    path = os.path.join(*args.d) if args.d else None

    if path:
        os.makedirs(path, exist_ok=True)

    if args.f:
        file_path = os.path.join(path, args.f) if path else args.f
        with open(file_path, "a") as file:
            if os.stat(file_path).st_size != 0:
                file.write("\n")

            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                new_line = input("Enter content line: ")
                if new_line == "stop":
                    break
                file.write(new_line + "\n")


if __name__ == "__main__":
    create_file()
