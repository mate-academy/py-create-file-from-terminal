import os
import argparse
from datetime import datetime


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_path: str) -> None:
    create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    exist_file = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if exist_file:
            file.write("\n\n")
        file.write(create_time + "\n")

        line_count = 0
        print("Enter content (use 'stop' to finish editing):")
        while True:
            line_count += 1
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_count} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create file with content"
    )
    parser.add_argument(
        "-d",
        dest="directory",
        nargs="+",
        help="Creates directory",
        default=None
    )
    parser.add_argument(
        "-f",
        dest="file_name",
        help="File name"
    )
    args = parser.parse_args()

    if not args.directory and not args.file_name:
        print("Please provide either -d or -f flag.")
        return

    if args.directory:
        directory = os.path.join(*args.directory)
        create_directory(directory)
        if args.file_name:
            file_path = os.path.join(directory, args.file_name)
            create_file(file_path)
    else:
        file_path = os.path.join(args.file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
