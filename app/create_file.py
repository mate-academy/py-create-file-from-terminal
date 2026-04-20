import os
import datetime
import argparse
import sys

parser = argparse.ArgumentParser("create_file_from_terminal")
parser.add_argument(
    "-f",
    metavar="filename",
    nargs="+",
    help="creates file in current directory"
)
parser.add_argument(
    "-d",
    metavar="dir_name",
    nargs="+",
    help="creates directories with provided path in form of dir1 dir2 dir3"
)
args = parser.parse_args()


def creates_directories() -> None:
    directories_path = os.path.join(*args.d)
    if not os.path.exists(directories_path):
        os.makedirs(directories_path)


def creates_file_path() -> str:
    if args.f and args.d:
        return os.path.join(*args.d, *args.f)
    elif args.f:
        return os.path.join(*args.f)
    elif args.d:
        return os.path.join(*args.d)


def creates_file(path: str) -> None:
    with open(path, "a") as file_out:
        if file_out.tell() != 0:
            file_out.write("\n")
        user_input = []
        while True:
            prompt_user_input = input("Enter content line: ")
            if prompt_user_input == "stop":
                break
            user_input.append(prompt_user_input)
        if not user_input:
            sys.exit("You didn't provide any content!")

        current_time = datetime.datetime.now()
        date_str = current_time.strftime("%Y-%m-%d %H:%M:%S\n")
        file_out.write(date_str)
        for index, element in enumerate(user_input):
            file_out.write(f"{index + 1} {element}\n")


if __name__ == "__main__":
    path = creates_file_path()
    if args.f and args.d:
        creates_directories()
        creates_file(path)
    elif args.f:
        creates_file(path)
    elif args.d:
        creates_directories()
