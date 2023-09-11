import argparse
import datetime
import os


parser = argparse.ArgumentParser()

parser.add_argument("-d", dest="directories", nargs="*",
                    help="all items after this flag are parts of the path")
parser.add_argument("-f", dest="file_name", help="first item is the file name")

args = parser.parse_args()

parent_dir = os.getcwd()


def create_dirs(dirs: list) -> None:

    path = os.path.join(parent_dir, *dirs)

    os.makedirs(path)


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        content = []

        content_is_collecting = True
        number_of_lines = 1
        while content_is_collecting:

            input_line = input("Enter content line: ")

            if input_line == "stop":
                content_is_collecting = False
            else:
                content.append(f"{number_of_lines} {input_line}\n")
                number_of_lines += 1

        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.writelines(content)
        file.write("\n")


if args.directories and not args.file_name:
    create_dirs(args.directories)

if args.file_name and not args.directories:
    create_file(args.file_name)

if args.directories and args.file_name:
    create_dirs(args.directories)

    path_to_f = os.path.join(parent_dir, *args.directories, args.file_name)

    create_file(path_to_f)
