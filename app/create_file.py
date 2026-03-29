import os
import argparse

from datetime import datetime


def create_directory(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def write_file(file_name: str, directory: str = os.getcwd()) -> None:
    counter = 0
    timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{directory}.{file_name}", "a") as file:
        file.write(timer + "\n")
        while True:
            counter += 1
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{counter} {line} \n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*")
    parser.add_argument("-f")
    args = parser.parse_args()
    if args.d and args.f:
        write_file(args.f, create_directory(args.d))
    elif args.d:
        create_directory(args.d)
    elif args.f:
        write_file(args.f)


if __name__ == "__main__":
    main()
