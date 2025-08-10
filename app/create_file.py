from argparse import ArgumentParser
from datetime import datetime
import os


def create_file(file_path: str) -> None:
    mode = "a"

    with open(file_path, mode) as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")

        lines_count = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                f.write("\n")
                break

            f.write(f"{lines_count} {content}\n")
            lines_count += 1


def main() -> None:
    parser = ArgumentParser(
        description="Create directories and files with user input"
    )

    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        help="Create directory in current directory",
        type=str
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Create file in current directory",
        type=str
    )

    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        os.makedirs(directory_path, exist_ok=True)

    if args.file:
        if args.directory:
            file_path = os.path.join(directory_path, args.file)
        else:
            file_path = args.file

        create_file(file_path)


if __name__ == "__main__":
    main()
