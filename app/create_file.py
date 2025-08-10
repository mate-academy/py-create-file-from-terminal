import os
import argparse
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def prompt_content() -> list:
    lines = []
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        lines.append(f"{line_number} {content}")
        line_number += 1
    return lines


def create_file_with_content(filepath: str) -> None:
    file_exists = os.path.exists(filepath)

    with open(filepath, "a" if file_exists else "w") as f:
        timestamp = get_timestamp()
        f.write(f"{timestamp}\n")
        content_lines = prompt_content()
        f.write("\n".join(content_lines) + "\n\n")

    print(f"File created/updated at: {filepath}")


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a directory or file with content."
    )

    parser.add_argument(
        "-d", "--directory", nargs="+", help="Path to the directory to create."
    )
    parser.add_argument(
        "-f", "--file", help="Name of the file to create or update."
    )

    args = parser.parse_args()

    if not args.directory and not args.file:
        print("Error: Missing command. "
              "You must specify either a directory or a file.")
        parser.print_help()
        return

    directory_path = None
    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)

    if args.file:
        filepath = (os.path.join(directory_path, args.file)
                    if directory_path else args.file)
        create_file_with_content(filepath)


if __name__ == "__main__":
    main()
