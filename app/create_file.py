import os

import sys

from datetime import datetime

from typing import List


def create_file(
        directory: List[str],
        file_name: str,
        content: str
) -> None:
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write("\n\n" + timestamp + "\n")
            for i, line in enumerate(content.splitlines(), 1):
                f.write(f"{i} {line}\n")
    else:
        with open(file_path, "w") as f:
            f.write(timestamp + "\n")
            for i, line in enumerate(content.splitlines(), 1):
                f.write(f"{i} {line}\n")


def main() -> None:
    directory = None
    file_name = None

    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = sys.argv[directory_index:]
        if not ("-f" in sys.argv):
            os.makedirs(os.path.join(*directory), exist_ok=True)
            return
        file_name = "file.txt"

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        directory = None

    if "-d" in sys.argv and "-f" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = sys.argv[directory_index:file_index - 1]

    content = ""

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content += line + "\n"

    create_file(directory, file_name, content.strip())


if __name__ == "__main__":
    main()
