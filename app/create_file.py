import argparse
import os

from datetime import datetime


def create_dir_or_file(
        directory: list[str] | None, file_name: list[str] | None
) -> None:

    directory_path = os.getcwd()

    if directory:
        directory_path = os.path.join(directory_path, *directory)
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(directory_path, *file_name)

        count = 1
        text = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                text.append("\n")
                break

            text.append(f"{count} {content}")
            count += 1

        with open(file_path, "a") as file:

            file.write("\n".join(text))


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
