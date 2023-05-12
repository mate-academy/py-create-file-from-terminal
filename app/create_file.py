import os
from datetime import datetime
from argparse import ArgumentParser


def add_content() -> str:
    line = 1
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = date_time + "\n"

    while True:
        user_text = input("Enter content line: ")
        if user_text == "stop":
            return content

        content += f"{line} {user_text}\n"
        line += 1


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n" + add_content())

    else:
        with open(file_path, "w") as new_file:
            new_file.write(add_content())


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
        create_file(path_file)

    elif args.dir:
        create_dir(args.dir)
    elif args.file:
        create_file(args.file)


if __name__ == "__main__":
    create_directories_and_file()
