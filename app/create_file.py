import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> str:
    filepath = os.path.join(directory, filename)

    return filepath


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
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1

        directory = os.path.join(*sys.argv[dir_index : file_index - 1])
        filename = sys.argv[file_index]

        os.makedirs(directory, exist_ok=True)
        filepath = create_file(directory, filename)
        write_content(filepath)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory, exist_ok=True)

    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]

        filepath = create_file(os.getcwd(), filename)
        write_content(filepath)

    else:
        print("Invalid arguments. Use -d for directory or -f for file.")


if __name__ == "__main__":
    main()
