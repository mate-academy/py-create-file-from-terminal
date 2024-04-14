import argparse
import os


def create_dirs(dir1: str, dir2: str) -> None:
    os.makedirs(os.path.join(os.getcwd(), dir1, dir2), exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a file or directory.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--directory", nargs='+', help="Path to the directory to create.")
    group.add_argument("-f", "--file", help="Name of the file to create.")

    args = parser.parse_args()

    if args.directory:
        create_dirs(args.directory)
        print(f"Directory {'/'.join(args.directory)} created successfully.")
    elif args.file:
        create_dirs(args.file)
        print(f"File {args.file} created successfully.")
