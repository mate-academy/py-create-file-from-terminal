import os
import sys
from datetime import datetime
from typing import Optional


def create_file_content() -> str:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return "\n".join(content_lines)


def create_file(
        directory: Optional[str] = None,
        filename: Optional[str] = None
) -> None:
    if directory:
        os.makedirs(directory, exist_ok=True)
        os.chdir(directory)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if filename:
        with open(filename, "a" if os.path.exists(filename) else "w") as file:
            file.write("\n\n" + timestamp + "\n")
            file.write(create_file_content())
            print(f"File {filename} created successfully.")
    else:
        print(f"Directory {directory} created successfully.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py -d [directory_path] -f [filename]")
        return

    args = sys.argv[1:]
    directory = None
    filename = None

    if "-d" in args:
        directory_index = args.index("-d") + 1
        directory = os.path.join(*args[directory_index:])
    if "-f" in args:
        filename_index = args.index("-f") + 1
        filename = args[filename_index]

    create_file(directory, filename)


if __name__ == "__main__":
    main()
