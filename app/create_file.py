import argparse
import os
import sys
from datetime import datetime


def create_folder(path: list) -> str:
    path = "/".join(path)
    os.makedirs(path, exist_ok=True)
    return path


def input_text(full_path: str) -> None:
    if not os.path.exists(full_path):
        mode = "w"
    else:
        mode = "a"
    with open(full_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        stop = "stop"
        it = 1
        while True:
            text = input("Enter content line: ")
            if text == stop:
                break
            file.write(str(it) + " " + text + "\n")
            it += 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="+"
    )
    parser.add_argument("-f")

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    parsed_args = parser.parse_args()
    if parsed_args.d is not None and parsed_args.f is not None:
        full_path = os.path.join(create_folder(parsed_args.d), parsed_args.f)
        input_text(full_path)
        return 0

    if parsed_args.d is not None:
        create_folder(parsed_args.d)

    if parsed_args.f is not None:
        input_text(parsed_args.f)

    return 0


if __name__ == "__main__":
    main()
