import argparse
import os

from datetime import datetime


def create_dir_or_file(
        directory: list[str] | None, file_name: list[str] | None
) -> None:

    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if file_name:
        file_path = os.path.join(directory_path, *file_name)
        write_to_file(file_path)


def write_to_file(file_path: str) -> None:
    count = 1

    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                file.write("\n")
                break

            file.write(str(count) + " " + content + "\n")
            count += 1


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--directory", nargs="+", help="Create a directory"
    )
    parser.add_argument("-f", "--file", nargs="+", help="Create a file")

    args = parser.parse_args()

    create_dir_or_file(args.directory, args.file)


if __name__ == "__main__":
    main()
