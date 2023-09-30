import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)

    file_path = os.path.join(directory, filename)

    content = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input()
        if line == "stop":
            break
        content.append(line)

    with open(file_path, "a") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_file.py [-d <directory>] -f <filename>")
        sys.exit(1)

    directory = ""
    filename = ""

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        directory = os.path.join(
            *sys.argv[d_index + 1:
                      d_index + 1
                      + sys.argv[d_index + 1:].index("-f")])

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        filename = sys.argv[f_index + 1]

    create_file(directory, filename)
