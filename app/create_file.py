import os
import argparse
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", dest="dirs")
    parser.add_argument("-f", dest="file")
    path = ""
    args = parser.parse_args()

    if args.dirs:
        path = os.path.join(path, *args.dirs)
        os.makedirs(path, exist_ok=True)
    if args.file:
        path = os.path.join(path, args.file)
        with open(path, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            line_index = 1
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                f.write(f"{line_index} {text}\n")
                line_index += 1


if __name__ == "__main__":
    create_file()
