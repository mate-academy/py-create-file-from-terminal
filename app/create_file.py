import os
import sys
from datetime import datetime
from typing import List


def create_file(file_path: str, content_lines: List[str]) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(content_lines, start=1):
            file.write(f"{idx} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py [-d directory] -f filename")
        return

    content_lines = []
    file_path = ""

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, sys.argv[-1])
    elif "-f" in sys.argv:
        file_path = sys.argv[-1]
    else:
        print("Usage: python create_file.py [-d directory] -f filename")
        return

    print(f"Creating file: {file_path}")

    while True:
        content_line = input("Enter content line (type 'stop' to finish): ")
        if content_line.lower() == "stop":
            break
        content_lines.append(content_line)

    if os.path.exists(file_path):
        print(f"Appending content to existing file: {file_path}")
    else:
        print(f"Creating new file: {file_path}")

    create_file(file_path, content_lines)
    print("File creation complete.")


if __name__ == "__main__":
    main()
