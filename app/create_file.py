import os
from datetime import datetime
from argparse import ArgumentParser


def create_file_and_content(file_path: str) -> None:
    line = 1
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(date_time + "\n")

        while True:
            user_text = input("Enter content line: ")
            if user_text == "stop":
                break
            file.write(f"{line} {user_text}\n")
            line += 1
        file.write("\n")


def create_dir(dirs: list) -> None:
    dirs = os.path.join(*dirs)
    os.makedirs(dirs, exist_ok=True)


def create_directories_and_file() -> None:
    parser = ArgumentParser(description="Create a directories and files")
    group = parser.add_argument_group()
    group.add_argument("-d", "--dir", nargs="+")
    group.add_argument("-f", "--file")

    args = parser.parse_args()
    if args.dir and args.file:
        path_file = os.path.join(*args.dir, args.file)
        create_dir(args.dir)
        create_file_and_content(path_file)

    elif args.dir:
        create_dir(args.dir)
    elif args.file:
        create_file_and_content(args.file)


if __name__ == "__main__":
    create_directories_and_file()
