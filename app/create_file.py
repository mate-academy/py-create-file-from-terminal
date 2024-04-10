import argparse
import os


from datetime import datetime


def create_dir(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path)


def create_file(directory: str, name: str) -> None:
    if directory:
        name = os.path.join(*directory, name)
    else:
        name = os.path.join(name)

    formatted_datetime = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    with open(name, "a") as file:
        count_number = 1
        file.write(formatted_datetime + "\n")
        while True:
            user_input = str(input(
                'Write your string (or "stop" for ending): '))
            if user_input.lower() == "stop":
                break
            file.write(f"{count_number} {user_input} + \n")
            count_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and file.")
    parser.add_argument("-d", "--directory",
                        nargs="*", help="Directory path to create")
    parser.add_argument("-f", "--file",
                        help="File to create")

    args = parser.parse_args()

    if args.directory:
        create_dir(args.directory)

    create_file(args.directory, args.file)


if __name__ == "__main__":
    main()
