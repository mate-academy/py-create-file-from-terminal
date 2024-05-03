from datetime import datetime
import os
import argparse


def create_directory(directory_name: list[str]) -> None:
    path = os.path.join(*directory_name)
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")


def create_file(
        file_name: str,
        content: list[str],
        directory_name: str = ""
) -> None:
    path = os.path.join(*directory_name, file_name)
    try:
        with open(path, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for line in content:
                file.write(f"{line}\n")
            file.write("\n")  # Add a blank line between data
    except OSError as e:
        print(f"Error creating file: {e}")


def get_user_input_content() -> list[str]:
    user_input = []
    line_number = 1
    while True:
        content = input("Enter content line (type 'stop' to finish): ")
        if content.lower() == "stop":
            break
        user_input.append(f"{line_number} {content}")
        line_number += 1
    return user_input


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
        user_content = get_user_input_content()
        create_file(file_name, user_content, directory_paths)


if __name__ == "__main__":
    main()
