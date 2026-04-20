import os
import argparse
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def provide_content() -> list:
    lines_content = []
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        lines_content.append(f"{line_number} {content}")
        line_number += 1
    return lines_content


def create_file_with_content(filepath: str) -> None:
    file_exists = os.path.exists(filepath)

    with open(filepath, "a" if file_exists else "w") as f:
        timestamp = get_timestamp()
        f.write(f"{timestamp}\n")
        content_lines = provide_content()
        f.write("\n".join(content_lines) + "\n\n")

    print(f"File created/updated at {filepath}")


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory created at: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a directory or file with content."
    )

    parser.add_argument(
        "-d", nargs="+", help="Path to the directory to create."
    )
    parser.add_argument(
        "-f", help="Name of the file to create or update."
    )

    args = parser.parse_args()

    if not args.d and not args.f:
        print("Error: Missing command.\n You must specify: directory/file")
        parser.print_help()
        return

    directory_path = None
    if args.d:
        directory_path = str(os.path.join(*args.d))
        create_directory(directory_path)

    if args.f:
        filepath = str((os.path.join(directory_path, args.f)
                        if directory_path else args.f))
        create_file_with_content(filepath)


if __name__ == "__main__":
    main()
