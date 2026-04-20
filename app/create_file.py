import os
import argparse
from datetime import datetime


def create_file_path(directory: str, filename: str) -> str:
    return os.path.join(directory, filename)


def create_directory(directory: str, **kwargs) -> None:
    os.makedirs(directory, **kwargs)


def write_content(filepath: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file:
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content_line = input(f"Enter content: Line{line_number} ")

            if content_line.lower() == "stop":
                break

            file.write(f"Line{line_number} {content_line}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content."
    )
    parser.add_argument("-d", nargs="*", help="Directory path")
    parser.add_argument("-f", help="File name")

    args = parser.parse_args()

    if args.d and args.f:
        directory = os.path.join(*args.d)
        filename = args.f

        create_directory(directory, exist_ok=True)
        filepath = create_file_path(directory, filename)
        write_content(filepath)

    elif args.d:
        directory = os.path.join(*args.d)
        create_directory(directory, exist_ok=True)

    elif args.f:
        filepath = create_file_path(os.getcwd(), args.f)
        write_content(filepath)

    else:
        print("Invalid arguments. Use -d for directory or -f for file.")


if __name__ == "__main__":
    main()
