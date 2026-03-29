import os
from datetime import datetime
from argparse import ArgumentParser


def create_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                file.write("\n")
                break
            file.write(f"{input_line}\n")


def create_dir_and_file_from_terminal() -> None:
    parser = ArgumentParser()

    parser.add_argument("-d", nargs="*")
    parser.add_argument("-f")

    args = parser.parse_args()

    path = ""
    if args.d is not None:
        path = os.path.join(*args.d)
        os.makedirs(path, exist_ok=True)
    if args.f is not None:
        path = os.path.join(path, args.f)
        create_file(path)


if __name__ == "__main__":
    create_dir_and_file_from_terminal()
