import argparse
import os
from datetime import datetime


def prompt_for_content() -> list[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def create_directory(path_parts: list[str]) -> str:
    try:
        directory_path = os.path.join(*path_parts)
        os.makedirs(directory_path, exist_ok=True)
        return directory_path
    except PermissionError:
        print("Permission denied: unable to create directory.")
    except Exception as e:
        print(f"An error occurred creating "
              f"directory: {e}")


def create_file(file_name: str, directory: str = None) -> None:
    try:
        if directory:
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name

        content_lines = prompt_for_content()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "w") as file:
            file.write(timestamp + "\n")
            for idx, line in enumerate(content_lines, start=1):
                file.write(f"{idx} {line}\n")

        print(f"File {file_name} created")
    except PermissionError:
        print("Permission denied: unable to create or write to file.")
    except Exception as e:
        print(f"An error occurred creating or "
              f"writing to file: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and files."
    )
    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        help="Directory path parts",
        default=[]
    )
    parser.add_argument("-f", "--file", help="File name")

    args = parser.parse_args()

    directory = None
    if args.directory:
        directory = create_directory(args.directory)

    if args.file:
        create_file(args.file, directory)


if __name__ == "__main__":
    main()
