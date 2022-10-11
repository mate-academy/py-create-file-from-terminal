import argparse
import os
import datetime
import sys


def file_content() -> str:
    print(sys.argv)
    xx = datetime.datetime.now()
    time_print = xx.strftime("%Y-%m-%d %X\n")
    return time_print


def create_directory(path_parts: str) -> str:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(file_name: str) -> str:
    with open(file_name, "a") as file:
        file.write(file_content())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories or files using flags."
    )
    parser.add_argument(
        "-d", "--directory", nargs="+",
        help="Create directory at specified path"
    )
    parser.add_argument(
        "-f", "--file", nargs=1,
        help="Create file with specified name and content"
    )
    args = parser.parse_args()
    if args.directory:
        if args.file:
            create_directory(args.directory)
            file_name = os.path.join(*args.directory, args.file[0])
            create_file(file_name)
            correct_file(args)
        else:
            create_directory(args.directory)
    elif args.file:
        file_name = args.file[0]
        create_file(file_name)
        correct_file(args)

    else:
        print("No action specified. Use -d or -f flag.")


def correct_file(args: str) -> None:
    line = "  "
    content = ""
    nn = 0
    while line != "stop":
        nn += 1
        line = input("Enter content line: ")
        if line != "stop":
            line = f"{nn} Line{nn} content \n"
            print(f"Line{nn} content")
            content += line
    if args.directory:
        created_directory = create_directory(args.directory)
        os.chdir(created_directory)
    with open("file.txt", "a") as f:
        f.write("".join(content))


if __name__ == "__main__":
    main()
