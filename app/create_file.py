import os
import sys
from datetime import datetime


def create_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file:
        file.write(content)


def main() -> None:
    directory_path = "."
    file_index = sys.argv.index("-f")
    if len(sys.argv) < 2:
        print(
            "Usage: python create_file.py -d <directory_path> -f <file_name>")
        return

    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d")
        if directory_index + 1 >= len(sys.argv):
            print("Please provide a directory path after -d flag.")
            return

        directory_path = os.path.join(
            *sys.argv[directory_index + 1:file_index]
        )
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        if file_index + 1 >= len(sys.argv):
            print("Please provide a file name after -f flag.")
            return

        file_name = sys.argv[file_index + 1]
        file_path = os.path.join(
            directory_path, file_name
        ) if "-d" in sys.argv else file_name

        if os.path.exists(file_path):
            print(f"Appending content to {file_path}:")
        else:
            print(f"Creating new file {file_path}:")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_file(file_path, f"\n{timestamp}")

        line_number = 1
        while True:
            line = input(
                f"{line_number} Enter content line (type 'stop' to finish): "
            )
            if line == "stop":
                break
            create_file(file_path, f"\n{line_number} {line}")
            line_number += 1


if __name__ == "__main__":
    main()
