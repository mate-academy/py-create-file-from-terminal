import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    filepath = os.path.join(directory, filename)

    if os.path.exists(filepath):
        print(f"File '{filename}' already exists. Adding content below:")
    else:
        print(f"Creating file '{filename}' in directory '{directory}'.")

    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content_line = input(
                f"Enter content line {line_number} (type 'stop' to finish): "
            )
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1

    print(f"File '{filename}' has been created/updated with content.")


def create_directory_and_file(
        base_directory: str,
        directory_parts: list,
        filename: str
) -> None:
    current_directory = os.path.join(base_directory, *directory_parts)
    os.makedirs(current_directory, exist_ok=True)
    print(f"Directory '{current_directory}' has been created.")
    if filename:
        create_file(current_directory, filename)


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1

        base_directory = os.getcwd()
        if dir_index < file_index:
            directory_parts = sys.argv[dir_index:file_index - 1]
            filename = sys.argv[file_index]
            create_directory_and_file(
                base_directory, directory_parts, filename
            )

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1

        base_directory = os.getcwd()
        directory_parts = sys.argv[dir_index:]

        create_directory_and_file(base_directory, directory_parts, "")

    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1

        base_directory = os.getcwd()
        filename = sys.argv[file_index]

        create_file(base_directory, filename)
