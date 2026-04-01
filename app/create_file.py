import argparse
import datetime
import os


parent_dir = os.getcwd()

parser = argparse.ArgumentParser()

parser.add_argument("-d", dest="directories", nargs="*", default=[],
                    help="all items after this flag are parts of the path")
parser.add_argument("-f", dest="file_name", help="first item is the file name")

args = parser.parse_args()


def create_dirs(dirs: list) -> None:
    path = os.path.join(parent_dir, *dirs)
    os.makedirs(path, exist_ok=True)


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        content = []
        number_of_lines = 1
        while True:

            input_line = input("Enter content line: ")

            if input_line == "stop":
                break
            else:
                content.append(f"{number_of_lines} {input_line}\n")
                number_of_lines += 1

        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.writelines(content)
        file.write("\n")


def main() -> None:
    create_dirs(args.directories)

    if args.file_name:
        path_to_file = os.path.join(
            parent_dir, *args.directories, args.file_name
        )
        create_file(path_to_file)


main()
