from datetime import datetime
import os
import argparse
import sys


def create_directory(directory_name: list[str]) -> None:
    path = os.path.join(*directory_name)
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")
        sys.exit(1)


def get_user_input_content(file) -> list[str]:
    user_input = []
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")  # Write timestamp
    while True:
        content = input("Enter content line (type 'stop' to finish): ")
        if content.lower() == "stop":
            break
        user_input.append(content)
    return user_input


def create_file(file_name: str, directory_name: str = "") -> None:
    path = os.path.join(*directory_name, file_name)
    try:
        with open(path, "a") as file:
            user_input = get_user_input_content(file)
            for line_number, content in enumerate(user_input, start=1):
                file.write(f"{line_number} {content}\n")
            file.write("\n")  # Add a blank line between data
    except OSError as e:
        print(f"Error creating file: {e}")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--directory",
                        help="Directory path",
                        nargs="+",
                        default="")
    parser.add_argument("-f",
                        "--filename",
                        help="File name",
                        default="")

    args = parser.parse_args()

    directory_paths = args.directory
    file_name = args.filename

    if directory_paths:
        create_directory(directory_paths)

    if file_name:
        create_file(file_name, directory_paths)


if __name__ == "__main__":
    main()
