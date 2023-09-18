import os
import sys
from datetime import datetime


def create_file_with_content(file_path: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_count = 1
    while True:
        content_line = input("Enter content line (or 'stop' to finish): ")
        if content_line.lower() == "stop":
            break
        with open(file_path, "a") as file:
            file.write(f"{line_count} {content_line}\n")
        line_count += 1

    with open(file_path, "r") as file:
        content = file.read()

    with open(file_path, "w") as file:
        file.write(f"{timestamp}\n")
        file.write(content)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py"
              " [-d <directory_path>] [-f <file_name>]")
        return
    directory_path = ""

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        directory_path = os.path.join(*sys.argv[dir_index + 1: f_index])
        os.makedirs(directory_path, exist_ok=True)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]

        if "-d" in sys.argv:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        if os.path.exists(file_path):
            print(f"File '{file_path}' already exists. Appending content.")
        else:
            print(f"Creating file {file_path}.")

        create_file_with_content(file_path)
        print(f"File {file_path} has been created with content.")


if __name__ == "__main__":
    main()
